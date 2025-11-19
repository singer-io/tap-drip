class dripError(Exception):
    """class representing Generic Http error."""

    def __init__(self, message=None, response=None):
        super().__init__(message)
        self.message = message
        self.response = response


class dripBackoffError(dripError):
    """class representing backoff error handling."""
    pass

class dripBadRequestError(dripError):
    """class representing 400 status code."""
    pass

class dripUnauthorizedError(dripError):
    """class representing 401 status code."""
    pass


class dripForbiddenError(dripError):
    """class representing 403 status code."""
    pass

class dripNotFoundError(dripError):
    """class representing 404 status code."""
    pass

class dripConflictError(dripError):
    """class representing 409 status code."""
    pass

class dripUnprocessableEntityError(dripBackoffError):
    """class representing 422 status code."""
    pass

class dripRateLimitError(dripBackoffError):
    """class representing 429 status code."""
    pass

class dripInternalServerError(dripBackoffError):
    """class representing 500 status code."""
    pass

class dripNotImplementedError(dripBackoffError):
    """class representing 501 status code."""
    pass

class dripBadGatewayError(dripBackoffError):
    """class representing 502 status code."""
    pass

class dripServiceUnavailableError(dripBackoffError):
    """class representing 503 status code."""
    pass

ERROR_CODE_EXCEPTION_MAPPING = {
    400: {
        "raise_exception": dripBadRequestError,
        "message": "A validation exception has occurred."
    },
    401: {
        "raise_exception": dripUnauthorizedError,
        "message": "The access token provided is expired, revoked, malformed or invalid for other reasons."
    },
    403: {
        "raise_exception": dripForbiddenError,
        "message": "You are missing the following required scopes: read"
    },
    404: {
        "raise_exception": dripNotFoundError,
        "message": "The resource you have specified cannot be found."
    },
    409: {
        "raise_exception": dripConflictError,
        "message": "The API request cannot be completed because the requested operation would conflict with an existing item."
    },
    422: {
        "raise_exception": dripUnprocessableEntityError,
        "message": "The request content itself is not processable by the server."
    },
    429: {
        "raise_exception": dripRateLimitError,
        "message": "The API rate limit for your organisation/application pairing has been exceeded."
    },
    500: {
        "raise_exception": dripInternalServerError,
        "message": "The server encountered an unexpected condition which prevented" \
            " it from fulfilling the request."
    },
    501: {
        "raise_exception": dripNotImplementedError,
        "message": "The server does not support the functionality required to fulfill the request."
    },
    502: {
        "raise_exception": dripBadGatewayError,
        "message": "Server received an invalid response."
    },
    503: {
        "raise_exception": dripServiceUnavailableError,
        "message": "API service is currently unavailable."
    }
}
