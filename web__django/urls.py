# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib.auth.views import logout, login
from django.contrib.staticfiles.views import serve

from firestorm.views_dutils import load_dutils_js
from firestorm.views import home
from firestorm.forms import CustomAuthForm


urlpatterns = [
    # These are Django canned pages
    url(r'^accounts/logout/$', logout, {'next_page': '/'},
        name='logout'),
    url(r'^accounts/login/$', login, {'template_name': 'login.html',
                                      'authentication_form': CustomAuthForm}),

    # This is the frowned-upon way of serving static files in Django
    url(r'^static/(?P<path>.*)$', serve, {'insecure': True}),

    # an awesome library for using named urls from within Javascript
    url(r'^js/dutils.conf.urls.js$', load_dutils_js,
        name='dutils_conf'),

    # These are custom to the Firestorm project
    url(r'^$', home,
        name='home'),
]
