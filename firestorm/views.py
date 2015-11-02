# -*- coding: utf-8 -*-
"""views.py represents the user-interface Pythonic logic.

This is the views.py which represents the Python logic for views
that refer specifically to a user's interaction with the application.
Kiosk views are held in another file and do not belong in here.
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """home is the main entrypoint of the user experience.

    I suspect this will ultimately have some sort of dashboard that allows
    the end-user to then make changes to the content presented to him/her.
    """
    return render(request, 'user/home.html', {})
