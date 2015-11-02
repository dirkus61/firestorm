# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User


class AutoEmailLoginBackend(object):
    """Authenticate against the custom user model with an email unique field.
    """
    @staticmethod
    def authenticate(email=None):
        """Determine if the user exists.  If not, create one.

        Either way, we return the new User instance.
        """
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Create a new user.
            user = User(email=email)
            user.save()
        return user

    @staticmethod
    def get_user(user_id):
        """Get the current User object with pk user_id"""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
