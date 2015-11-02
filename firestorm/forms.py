# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst


class CustomAuthForm(forms.Form):
    """Custom class for authenticating users. Extend this to get a form that
    accepts email logins.
    """
    email = forms.CharField(max_length=254)

    error_messages = {
        'invalid_login': ("Please enter a correct %(email)s. "
                          "Note that the field may be case-sensitive."),
        'inactive': ("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(CustomAuthForm, self).__init__(*args, **kwargs)

        # Set the label for the "email" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        email = self.cleaned_data.get('email')

        if email:
            self.user_cache = authenticate(email=email)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'email': self.email_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


