#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sato_format_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from base.models.displayable_mixin import DisplayableMixin


class SatoFormatModel(DisplayableMixin):
    """SatoFormatModel

    SatoFormatModel is a DisplayableMixin.
    Responsibility:
    """
    title = models.CharField(
        _('format name'),
        max_length=255,
        null=False,
        blank=False,
    )
    description = RichTextField(
        _('description'),
        config_name='simple',
        default='',
        blank=True,
    )
    file = models.FileField(
        'PDF',
        upload_to='formats',
        null=True,
        blank=True,
        default=None,
    )
    form = models.URLField(
        _('form address'),
        max_length=200,
        null=True,
        blank=True,
        default=None,
    )
    sortid = models.IntegerField(
        u' ',
        default=0,
        blank=False,
        null=False,
        db_index=True,
        help_text=u'サイトで昇順に並びます',
    )

    class Meta:
        verbose_name = _('Sato Formats')
        verbose_name_plural = _('Sato Formats')
        ordering = ['sortid', ]

    def __str__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sato_format_model.py ends here
