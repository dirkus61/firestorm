# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello World')