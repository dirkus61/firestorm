# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
from __future__ import unicode_literals


class MyAppRouter(object):
    """A router to control all database operations on models"""
    def db_for_read(self, model, **hints):
        """Point all operations on myapp models to 'other'"""
        if hasattr(model, 'db_name'):
            return model.db_name
        return 'default'

    def db_for_write(self, model, **hints):
        """Point all operations on myapp models to 'other'"""
        if hasattr(model, 'db_name'):
            return model.db_name
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, model):
        if hasattr(model, 'db_name'):
            if model.db_name == db:
                return True
            return False
        if db == 'default':
            return True
        return False
