#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_query_set --

"""
from django.db.models.query import QuerySet


class EventQuerySet(QuerySet):
    """EventQuerySet

    EventQuerySet is a QuerySet.
    Responsibility:
    """
    def confirmed(self, ):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        return self.filter(status=EVENT_CONFIRMED_STATUS)

    def between_date(self, start, end):
        r"""SUMMARY

        between_date(start, end)

        @Arguments:
        - `start`:
        - `end`:

        @Return:

        @Error:
        """
        if end < start:
            start = end
        return self.filter(date__gte=start, date__lte=end)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_query_set.py ends here
