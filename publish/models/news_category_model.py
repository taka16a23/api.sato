#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""お知らせカテゴリーモデル --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from colorfield.fields import ColorField


class NewsCategoryModel(models.Model):
    """NewsCategoryModel

    NewsCategoryModel is a models.Model.
    Responsibility:
    """
    # カテゴリー名
    name = models.CharField(
        _('category name'),
        max_length=8,
        unique=True,
        null=False,
        blank=False,
        help_text=_('8文字以内'),
    )
    # 文字色
    fgcolor = ColorField(
        _('foreground color'),
        default='#ffffff',
    )
    # 背景色
    bgcolor = ColorField(
        _('background color'),
        default='#ff0000',
    )
    # 並び順
    sortid = models.IntegerField(
        _('sort key'),
        default=0,
        blank=False,
        null=False,
        db_index=True,
        help_text=_('sort by ascending'),
    )

    class Meta:
        verbose_name = _('news category')
        verbose_name_plural = _('news category')
        ordering = ['sortid', ]

    def __str__(self):
        return self.name



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_category_model.py ends here
