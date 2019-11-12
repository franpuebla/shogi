from flask import jsonify
from .endpoints import custom_api

class GenericException(Exception):
    def __init__(self, message, status_code=None, payload=None):
        super(GenericException, self).__init__()

        if status_code is not None:
            self.status_code = status_code

        if message is not None:
            self.message = message

        self.payload = payload
        self.headers = None
        if self.payload is not None and self.payload['headers'] is not None and self.payload['headers'] != '':
            self.headers = self.payload['headers']

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class InternalServerErrorException(GenericException):
    status_code = 500
    message = 'An internal server error has ocurred.'

    def __init__(self, message=None, status_code=None, payload=None):
        super(InternalServerErrorException, self).__init__(message, status_code, payload)

def handle_exceptions(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    if not error.headers is None:
        response.headers = error.headers
    return response

@custom_api.errorhandler(InternalServerErrorException)
def handle_internal_server_error(error):
    return handle_exceptions(error)

class BadRequestException(GenericException):
    status_code = 400
    message = 'Bad Request.'

    def __init__(self, message=None, status_code=None, payload=None):
        super(BadRequestException, self).__init__(message, status_code, payload)

@custom_api.errorhandler(BadRequestException)
def handle_bad_request(error):
    return handle_exceptions(error)

class NotFoundException(GenericException):
    status_code = 404
    message = 'Not Found Error.'

    def __init__(self, message=None, status_code=None, payload=None):
        super(NotFoundException, self).__init__(message, status_code, payload)

@custom_api.app_errorhandler(NotFoundException)
def page_not_found(error):
    response = jsonify({'error': 'Not Found'})
    response.status_code = 404
    return response

class ForbiddenException(GenericException):
    status_code = 403
    message = 'Forbidden Exception.'

    def __init__(self, message=None, status_code=None, payload=None):
        super(ForbiddenException, self).__init__(message, status_code, payload)

@custom_api.errorhandler(ForbiddenException)
def handle_bad_request(error):
    return handle_exceptions(error)

class NotAuthorizedException(GenericException):
    status_code = 401
    message = 'Not Authorized.'

    def __init__(self, message=None, status_code=None, payload=None):
        super(NotAuthorizedException, self).__init__(message, status_code, payload)

@custom_api.errorhandler(NotAuthorizedException)
def handle_not_authorized(error):
    return handle_exceptions(error)
