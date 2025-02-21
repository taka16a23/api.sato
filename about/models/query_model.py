#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""query_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from db_stamp.models.timestamp_mixin import TimeStampMixin


class QueryStatusChoices(models.TextChoices):
    """QueryStatusChoices

    QueryStatusChoices is a models.TextChoices.
    Responsibility:
    """
    UNTREATED = '1', _('untreated')
    CONFIRMED = '2', _('confirmed')
    FINISHED = '3', _('finished')


class QueryModel(TimeStampMixin):
    """QueryModel

    QueryModel is a TimeStampMixin.
    Responsibility:
    """
    status = models.CharField(
        _('query status'),
        max_length=1,
        choices=QueryStatusChoices,
        default=QueryStatusChoices.UNTREATED,
    )
    name = models.CharField(
        _('name'),
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        _('mail address'),
        blank=False,
        null=False,
    )
    body = models.TextField(
        _('body'),
        blank=True,
        null=True,
    )

    class Meta(object):
        verbose_name = _('inquiries')
        verbose_name_plural = _('inquiries')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# query_model.py ends here
