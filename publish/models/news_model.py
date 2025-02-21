#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.displayable_mixin import DisplayableMixin
from publish.models.news_category_model import NewsCategoryModel


class NewsModel(DisplayableMixin):
    """NewsModel

    NewsModel is a DisplayableMixin.
    Responsibility:
    """
    # タイトル
    title = models.CharField(
        _('title'),
        max_length=200,
        blank=False,
        default='',
        help_text=_('news title'),
    )
    # カテゴリー
    category = models.ForeignKey(
        NewsCategoryModel,
        verbose_name=_('category'),
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        help_text=_('news category'),
    )
    # URL
    url = models.URLField(
        _('URL'),
        max_length=200,
        blank=False,
    )

    class Meta(object):
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_model.py ends here
