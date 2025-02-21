#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity_model --

"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from base.models.displayable_mixin import DisplayableMixin
from publish.models.news_model import NewsModel
from publish.models.news_category_model import NewsCategoryModel


class ActivityModel(DisplayableMixin):
    """ActivityModel

    ActivityModel is a DisplayableMixin.
    Responsibility:
    """
    title = models.CharField(
        _('title'),
        max_length=255,
        blank=False,
        default='',
        null=False,
    )
    image = models.ImageField(
        _('image'),
        upload_to='activity/images',
        blank=True,
        null=True,
    )
    body = models.TextField(
        _('body'),
        blank=True,
        null=True,
    )
    excerpt = models.TextField(
        _('Article excerpt'),
        blank=True,
        null=False,
        default='',
    )
    news = models.ForeignKey(
        NewsModel,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('create news if blank when first time')
    )

    class Meta:
        verbose_name = _('activities')
        verbose_name_plural = _('activities')

    def get_absolute_url(self, ):
        return '/activity/{}'.format(str(self.id))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity_model.py ends here
