from flask.ext.restless import ProcessingException
from functools import wraps
from flask import request
from flask import current_app
from api import app
# from api.api_0_1.models.model import db
from api.api_0_1.models.status import Status

class Views(object):
    """
    Views
    **Overview**

    Used to generalize attributes and methods for all views package.
    Properties needed to create an endpoint using restless-extension
    """

    preprocessors = None
    postprocessors = None
    url_prefix = '/0.1'
    methods = ['GET', 'POST', 'PATCH','DELETE']
    include_columns = None
    exclude_columns = None


    def __init__(self):
        self.preprocessors = {
            'GET_SINGLE': [self.get_single_preprocessor],
            'GET_MANY': [self.get_many_preprocessor],
            'POST': [self.post_preprocessor],
            'PATCH_SINGLE': [self.patch_single_preprocessor],
            'PATCH_MANY': [self.patch_many_preprocessor],
            'DELETE_SINGLE': [self.delete_single_preprocessor],
            'DELETE_MANY': [self.delete_many_preprocessor]
        }

        self.postprocessors = {
            'GET_SINGLE': [self.get_single_postprocessor],
            'GET_MANY': [self.get_many_postprocessor],
            'POST': [self.post_postprocessor],
            'PATCH_SINGLE': [self.patch_single_postprocessor],
            'PATCH_MANY': [self.patch_many_postprocessor],
            'DELETE_SINGLE': [self.delete_postprocessor],
            'DELETE_MANY': [self.delete_many_postprocessor]
        }

    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not Views.check_auth(auth.username, auth.password):
                return authenticate()
            return f(*args, **kwargs)
        return decorated

    @staticmethod
    def check_auth(username, password):
        import base64
        import md5
        """
        This function is called to check if a username /
        password combination is valid.
        """
        md5_user = md5.md5(app.config['GENERAL']['password'])

        try:
            decode_username = base64.b64decode(username)
        except:
            return False

        if decode_username == md5_user.hexdigest():
            return True
        else:
            return False

    @staticmethod
    def authenticate():
        """Sends a 401 response that enables basic auth"""
        raise ProcessingException(description='Unauthorized', code=401)

    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not Views.check_auth(auth.username, auth.password):
                return Views.authenticate()
            return f(*args, **kwargs)
        return decorated


    # Preprocessors
    @staticmethod
    @requires_auth
    def get_single_preprocessor(instance_id=None, **kw): pass

    @staticmethod
    @requires_auth
    def get_many_preprocessor(search_params=None, **kw): pass

    @staticmethod
    @requires_auth
    def post_preprocessor(data=None, **kw): pass

    @staticmethod
    @requires_auth
    def patch_single_preprocessor(instance_id=None, data=None, **kw): pass

    @staticmethod
    @requires_auth
    def patch_many_preprocessor(search_params=None, data=None, **kw): pass

    @staticmethod
    @requires_auth
    def delete_single_preprocessor(instance_id=None, **kw): pass

    @staticmethod
    @requires_auth
    def delete_many_preprocessor(search_params=None, **kw): pass


    # Postprocessors
    @staticmethod
    def get_single_postprocessor(result=None, **kw): pass
    @staticmethod
    def get_many_postprocessor(result=None, search_params=None, **kw): pass
    @staticmethod
    def post_postprocessor(result=None, **kw): pass
    @staticmethod
    def patch_single_postprocessor(result=None, **kw): pass
    @staticmethod
    def patch_many_postprocessor(query=None, data=None, search_params=None, **kw): pass
    @staticmethod
    def delete_postprocessor(was_deleted=None, **kw): pass
    @staticmethod
    def delete_many_postprocessor(result=None, search_params=None, **kw): pass
