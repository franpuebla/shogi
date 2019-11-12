#!/usr/bin/env python
"""Implements a shogi"""
from views import *
import ConfigParser
import subprocess
import re
import collections
import os
import time
import datetime
import thread
import requests
import random
import time

from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify
from flask import Blueprint
from flask import g
# from api.api_0_1.libs.chatbot_connector import Chatbotapi
# from api.api_0_1.libs.chatbot_connector import Waboxapp

from functools import wraps

custom_api = Blueprint('custom_api', __name__)
from .exceptions import *

def authenticate():
    """Sends a 401 response that enables basic auth"""
    raise NotAuthorizedException()

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        print(auth)
        if not auth or not Views.check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

#Comienzo API
@custom_api.route('/')
# @requires_auth
def api_root():
    message = {'status': 200, 'message': 'shogi'}
    resp = jsonify(message)
    resp.status_code = 200
    return resp

@custom_api.route('/board', methods=['GET'])
# @requires_auth
def board():
    # print request.headers
    print "   0  1  2  3  4  5  6  7  8  "
    print "+-----------------------------+"
    print "0| Lv Nv Sv Gv Kv Gv Sv Nv Lv |"
    print "1|    Rv                Bv    |"
    print "2| Pv Pv Pv Pv Pv Pv Pv Pv Pv |"
    print "3|                            |"
    print "4|                            |"
    print "5|                            |"
    print "6| P^ P^ P^ P^ P^ P^ P^ P^ P^ |"
    print "7|    B^                R^    |"
    print "8| L^ N^ S^ G^ K^ G^ S^ N^ L^ |"
    print "+-----------------------------+"
    # data = request.form
    # response = send(data)
    # return response

def __build_response_msg(endpoint=None, options={}):
   if 'status_code' not in options:
       raise InternalServerErrorException()

   default_options = {
       'status_code': '',
       'headers': None,
       'body': None,
       'content_type': None
   }
   default_options.update(options)

   if default_options['body'] is not None:
       default_options['content_type'] = 'application/json'

   ret = {}
   if endpoint is not None:
       ret[endpoint] = default_options['body']
       ret = json.dumps(ret)
   else:
       ret = json.dumps(default_options['body'])

   response = Response(
       response=ret,
       status=default_options['status_code'],
       content_type=default_options['content_type']
   )

   if default_options['headers'] is not None:
       for key, val in default_options['headers'].items():
           response.headers[key] = val

   return response
