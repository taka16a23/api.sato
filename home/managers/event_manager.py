#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_manager --

"""
from backend.base.managers.base_manager import BaseManager


class EventManager(BaseManager):
    """EventManager

    EventManager is a BaseManager.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return EventQuerySet(self.model)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_manager.py ends here
