class DripError(Exception):
    """class representing Generic Http error."""

    def __init__(self, message=None, response=None):
        super().__init__(message)
        self.message = message
        self.response = response


class DripBackoffError(DripError):
    """class representing backoff error handling."""
    pass

class DripBadRequestError(DripError):
    """class representing 400 status code."""
    pass

class DripUnauthorizedError(DripError):
    """class representing 401 status code."""
    pass


class DripForbiddenError(DripError):
    """class representing 403 status code."""
    pass

class DripNotFoundError(DripError):
    """class representing 404 status code."""
    pass

class DripConflictError(DripError):
    """class representing 409 status code."""
    pass

class DripUnprocessableEntityError(DripError):
    """class representing 422 status code."""
    pass

class DripRateLimitError(DripBackoffError):
    """class representing 429 status code."""
    def __init__(self, message=None, response=None):
        """Initialize the DripRateLimitError. Parses the rate limit headers from the response."""
        self.response = response
        self.retry_after = None
        self.limit = None
        self.remaining = None

        if response is not None:
            headers = response.headers or {}

            self.limit = headers.get('X-RateLimit-Limit') or headers.get('x-ratelimit-limit')
            self.remaining = headers.get('X-RateLimit-Remaining') or headers.get('x-ratelimit-remaining')

            retry_after_header = headers.get('Retry-After') or headers.get('retry-after')
            if retry_after_header:
                try:
                    self.retry_after = int(retry_after_header)
                except (ValueError, TypeError):
                    self.retry_after = 3600
            else:
                self.retry_after = 3600

        base_msg = message or "Drip API rate limit exhausted"
        retry_info = (
            f"(Retry after {self.retry_after} seconds.)"
            if self.retry_after is not None
            else "(Retry after unknown delay.)"
        )
        full_message = f"{base_msg} {retry_info}"
        super().__init__(full_message, response=response)

class DripInternalServerError(DripBackoffError):
    """class representing 500 status code."""
    pass

class DripNotImplementedError(DripError):
    """class representing 501 status code."""
    pass

class DripBadGatewayError(DripBackoffError):
    """class representing 502 status code."""
    pass

class DripServiceUnavailableError(DripBackoffError):
    """class representing 503 status code."""
    pass

class DripGatewayTimeoutError(DripBackoffError):
    """class representing 504 status code."""
    pass

ERROR_CODE_EXCEPTION_MAPPING = {
    400: {
        "raise_exception": DripBadRequestError,
        "message": "A validation exception has occurred."
    },
    401: {
        "raise_exception": DripUnauthorizedError,
        "message": "The access token provided is expired, revoked, malformed or invalid for other reasons."
    },
    403: {
        "raise_exception": DripForbiddenError,
        "message": "You are missing the following required scopes: read"
    },
    404: {
        "raise_exception": DripNotFoundError,
        "message": "The resource you have specified cannot be found."
    },
    409: {
        "raise_exception": DripConflictError,
        "message": "The API request cannot be completed because the requested operation would conflict with an existing item."
    },
    422: {
        "raise_exception": DripUnprocessableEntityError,
        "message": "The request content itself is not processable by the server."
    },
    429: {
        "raise_exception": DripRateLimitError,
        "message": "The API rate limit for your organisation/application pairing has been exceeded."
    },
    500: {
        "raise_exception": DripInternalServerError,
        "message": "The server encountered an unexpected condition which prevented" \
            " it from fulfilling the request."
    },
    501: {
        "raise_exception": DripNotImplementedError,
        "message": "The server does not support the functionality required to fulfill the request."
    },
    502: {
        "raise_exception": DripBadGatewayError,
        "message": "Server received an invalid response."
    },
    503: {
        "raise_exception": DripServiceUnavailableError,
        "message": "API service is currently unavailable."
    },
    504: {
        "raise_exception": DripGatewayTimeoutError,
        "message": "The server did not receive a timely response from an upstream server."
    }
}
