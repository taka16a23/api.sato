#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_request --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from db_stamp.models.timestamp_mixin import TimeStampMixin


class RoomChoices(models.TextChoices):
    """RoomChoices

    RoomChoices is a models.TextChoices.
    Responsibility:
    """
    BIG_ROOM = '1', _('Big Room')
    JAPANESE_STYLE_ROOM = '2', _('Japanese Style Room')
    NEIGHBORHOOD_HALL_2F = '3', _('Neighborhood hall 2F')


class HallRequestModel(TimeStampMixin):
    """HallRequestModel

    HallRequestModel is a models.Model.
    Responsibility:
    """
    group_name = models.CharField(
        _('group name'),
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    responsible_person = models.CharField(
        _('responsible person'),
        max_length=50,
        null=False,
        blank=False,
        default='',
    )
    address = models.CharField(
        _('address'),
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    phone_number = models.CharField(
        _('phone number'),
        max_length=50,
        null=False,
        blank=False,
        default='',
    )
    email_address = models.CharField(
        _('email address'),
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    reason = models.CharField(
        _('reson'),
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    start_datetime = models.DateTimeField(
        _('start datetime'),
        # null不許可
        null=False,
    )
    end_datetime = models.DateTimeField(
        _('end datetime'),
        # null不許可
        null=False,
    )
    room = models.CharField(
        _('room'),
        max_length=1,
        choices=RoomChoices,
        default=RoomChoices.BIG_ROOM,
    )
    detail = models.CharField(
        _('detail'),
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    note = models.TextField(
        _('note'),
        null=False,
        blank=False,
        default='',
    )
    is_finished = models.BooleanField(
        _('is finished'),
        null=False,
        blank=False,
        default=False,
    )

    class Meta:
        verbose_name = _('Hall Request')
        verbose_name_plural = _('Hall Request')
        ordering = ['created_at', ]

    def __str__(self):
        return self.group_name



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_request.py ends here
