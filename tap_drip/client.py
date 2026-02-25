from typing import Any, Dict, Mapping, Optional, Tuple

import backoff
import requests
from requests import session
from requests.exceptions import Timeout, ConnectionError, ChunkedEncodingError
from singer import get_logger, metrics

from tap_drip.exceptions import (
    ERROR_CODE_EXCEPTION_MAPPING,
    DripBackoffError,
    DripError,
    DripNotImplementedError,
    DripRateLimitError
)

LOGGER = get_logger()
REQUEST_TIMEOUT = 300

def wait_if_retry_after(exception_info):
    """
    Handle rate limit backoff by using the retry_after value from DripRateLimitError.
    Returns the number of seconds to wait.
    """
    exception = exception_info.get('exception') if isinstance(exception_info, dict) else exception_info

    if exception and isinstance(exception, DripRateLimitError):
        retry_after = exception.retry_after or 3600
        LOGGER.info(
            f"Rate limit hit. Waiting {retry_after} seconds. "
            f"Limit: {exception.limit}, Remaining: {exception.remaining}"
        )

        if exception.response:
            response = exception.response
            headers = response.headers or {}
            limit = headers.get('X-RateLimit-Limit')
            remaining = headers.get('X-RateLimit-Remaining')
            if limit and remaining:
                LOGGER.info(f"Rate limit info - Limit: {limit}, Remaining: {remaining}")

        return retry_after
    else:
        LOGGER.info("Rate limit hit. Waiting 3600 seconds (1 hour) as default.")
        return 3600

def raise_for_error(response: requests.Response) -> None:
    """Raises the associated response exception. Takes in a response object,
    checks the status code, and throws the associated exception based on the
    status code.

    :param resp: requests.Response object
    """
    try:
        response_json = response.json()
    except Exception:
        response_json = {}
    if response.status_code not in [200, 201, 204]:
        errors = response_json.get("errors", [])
        if errors and isinstance(errors, list) and len(errors) > 0:
            error_messages = []
            for error_obj in errors:
                error_code = error_obj.get("code", "unknown_error")
                error_message = error_obj.get("message", "Unknown Error")
                attribute = error_obj.get("attribute")
                if attribute:
                    error_messages.append(f"[{error_code}] {attribute}: {error_message}")
                else:
                    error_messages.append(f"[{error_code}] {error_message}")
            combined_errors = "; ".join(error_messages)
            message = f"HTTP-error-code: {response.status_code}, Errors: {combined_errors}"
        else:
            error_message = ERROR_CODE_EXCEPTION_MAPPING.get(
                response.status_code, {}
            ).get("message", "Unknown Error")
            message = f"HTTP-error-code: {response.status_code}, Error: {response_json.get('message', error_message)}"

        # For 5xx errors, use backoff exception if not specifically mapped
        if 500 <= response.status_code < 600:
            exc = ERROR_CODE_EXCEPTION_MAPPING.get(response.status_code, {}).get(
                "raise_exception", DripBackoffError
            )
        else:
            exc = ERROR_CODE_EXCEPTION_MAPPING.get(response.status_code, {}).get(
                "raise_exception", DripError
            )
        raise exc(message, response) from None


class Client:
    """
    A Wrapper class.
    ~~~
    Performs:
     - Authentication
     - Response parsing
     - HTTP Error handling and retry
    """

    def __init__(self, config: Mapping[str, Any]) -> None:
        self.config = config
        self._session = session()
        self._session.auth = (config.get("api_token"), "")
        self.base_url = "https://api.getdrip.com/v2"
        config_request_timeout = config.get("request_timeout")
        self.request_timeout = float(config_request_timeout) if config_request_timeout else REQUEST_TIMEOUT

    def __enter__(self):
        self.check_api_credentials()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._session.close()

    def check_api_credentials(self) -> None:
        pass

    def authenticate(self, headers: Dict, params: Dict) -> Tuple[Dict, Dict]:
        """Authenticates the request with the token"""
        return headers, params

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        path: Optional[str] = None
    ) -> Any:
        """
        Sends an HTTP request to the specified API endpoint.
        """
        params = params or {}
        headers = headers or {}
        body = body or {}
        endpoint = endpoint or f"{self.base_url}/{path}"
        headers, params = self.authenticate(headers, params)
        return self.__make_request(
            method, endpoint,
            headers=headers,
            params=params,
            data=body,
            timeout=self.request_timeout
        )

    @backoff.on_exception(
        backoff.expo,
        exception=(
            ConnectionResetError,
            ConnectionError,
            ChunkedEncodingError,
            Timeout,
            DripBackoffError,
        ),
        max_tries=5,
        factor=2,
        giveup=lambda e: isinstance(e, (DripNotImplementedError, DripRateLimitError)),
    )
    @backoff.on_exception(
        backoff.runtime,
        exception=(
            DripRateLimitError,
        ),
        max_tries=5,
        value=wait_if_retry_after,
        jitter=None
    )
    def __make_request(
        self, method: str, endpoint: str, **kwargs
    ) -> Optional[Mapping[Any, Any]]:
        """Performs HTTP Operations."""
        method = method.upper()
        with metrics.http_request_timer(endpoint):
            if method in ("GET", "POST"):
                if method == "GET":
                    kwargs.pop("data", None)
                response = self._session.request(method, endpoint, **kwargs)
                raise_for_error(response)
            else:
                raise ValueError(f"Unsupported method: {method}")

        return response.json()
