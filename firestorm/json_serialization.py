# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import decimal
import json

from django.http import HttpResponse


def json_dumps_with_datetime_and_decimal(data):
    # http://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript
    # http://stackoverflow.com/questions/16957275/python-to-json-serialization-fails-on-decimal
    def handler(obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder().default(obj)
    return json.dumps(data, default=handler)


def _JsonResponse(data):
    return HttpResponse(json_dumps_with_datetime_and_decimal(data),
                        content_type='application/json')


# http://stackoverflow.com/questions/12806386/standard-json-api-response-format
# http://labs.omniti.com/labs/jsend
def JsonSuccessResponse(data=None):
    if isinstance(data, str):
        data = json.loads(data)
    a = {'status': 'success',
         'data': data}
    return _JsonResponse(a)


# See this for how it might look for Django stuff:
# https://docs.djangoproject.com/en/1.8/ref/forms/api/#django.forms.Form.errors.as_json
def JsonFailResponse(data):
    if isinstance(data, str):
        data = json.loads(data)
    a = {'status': 'fail',
         'data': data}
    return _JsonResponse(a)


def JsonErrorResponse(message, data=None):
    if isinstance(data, str):
        data = json.loads(data)
    a = {'status': 'error',
         'message': message}
    if data:
        a['data'] = data
    return _JsonResponse(a)
