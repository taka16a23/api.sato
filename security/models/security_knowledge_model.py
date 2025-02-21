#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""security_knowledge_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from base.models.displayable_mixin import DisplayableMixin


class SecurityKnowledgeModel(DisplayableMixin):
    """SecurityKnowledgeModel

    SecurityKnowledgeModel is a DisplayableMixin.
    Responsibility:
    """
    title = models.CharField(
        _('title'),
        max_length=255,
        null=False,
        default='',
    )
    description = RichTextField(
        _('description'),
        config_name='simple',
        blank=True,
    )
    url = models.URLField(
        _('URL'),
        max_length=200,
        blank=False,
    )
    thumbnail = models.ImageField(
        _('thumbnail'),
        upload_to='knowledge/',
        blank=True,
        null=True,
    )
    sortid = models.IntegerField(
        ' ',
        default=0,
        blank=False,
        null=False,
        db_index=True,
        help_text=u'サイトで昇順に並びます',
    )

    class Meta:
        verbose_name = _('Security Knowledge')
        verbose_name_plural = _('Security Knowledge')
        ordering = ['sortid', ]

    def __str__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# security_knowledge_model.py ends here
