#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_request_receiver_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_stamp_mixin import BaseStampMixin


class HallRequestReceiverModel(BaseStampMixin):
    """HallRequestReceiverModel

    HallRequestReceiverModel is a BaseStampMixin.
    Responsibility:
    """
    name = models.CharField(
        _('name'),
        max_length=50,
        blank=True,
        null=True,
        default='',
    )
    email = models.EmailField(
        _('email'),
        blank=False,
        null=False,
        help_text=_('example@example.com'),
    )
    active = models.BooleanField(
        _('receive'),
        default=False,
    )

    class Meta(object):
        verbose_name = _('Hall Request Reciever')
        verbose_name_plural = _('Hall Request Reciever')
        ordering = ['name', ]

    def __str__(self):
        return self.name



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_request_receiver_model.py ends here
