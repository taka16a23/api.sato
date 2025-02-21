#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base_manager --

"""
from django.db.models import Manager


class BaseManager(Manager):
    """BaseManager

    BaseManager is a Manager.
    Responsibility:
    """
    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base_manager.py ends here
