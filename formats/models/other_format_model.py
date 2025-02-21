#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""other_format_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from base.models.displayable_mixin import DisplayableMixin


class OtherFormatModel(DisplayableMixin):
    """OtherFormatModel

    OtherFormatModel is a DisplayableMixin.
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
    url = models.URLField(
        _('URL'),
        max_length=200,
        null=False,
        blank=False,
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
        verbose_name = _('Other Formats')
        verbose_name_plural = _('Other Formats')
        ordering = ['sortid', ]

    def __str__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# other_format_model.py ends here
