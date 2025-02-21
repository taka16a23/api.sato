#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_event_model --

"""
from django.db import models


EVENT_CONFIRMED_STATUS = 1
EVENT_TENTATIVE_STATUS = 2
EVENT_CANCELLED_STATUS = 3

EVENT_STATUS = ((EVENT_CONFIRMED_STATUS, 'confirmed'),
                (EVENT_TENTATIVE_STATUS, 'tentative'),
                (EVENT_CANCELLED_STATUS, 'cancelled'), )


class HallEventModel(models.Model):
    """HallEventModel

    HallEventModel is a models.Model.
    Responsibility:
    """
    gid = models.TextField()
    summary = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date = models.DateField(
        null=True,
        blank=True,
    )
    url = models.URLField(
        null=True,
        blank=True,
    )
    status = models.IntegerField(
        choices=EVENT_STATUS,
        default=EVENT_CONFIRMED_STATUS,
    )
    start = models.DateTimeField(
        null=True,
    )
    end = models.DateTimeField(
        null=True,
    )
    created = models.DateTimeField(
        null=True,
    )
    modified = models.DateTimeField(
        null=True,
    )

    def __str__(self):
        return self.summary



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_event_model.py ends here
