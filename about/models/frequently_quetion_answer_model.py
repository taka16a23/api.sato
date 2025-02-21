#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""frequently_quetion_answer_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from base.models.displayable_mixin import DisplayableMixin


class FrequentlyQuetionAnswerModel(DisplayableMixin):
    """FrequentlyQuetionAnswerModel

    FrequentlyQuetionAnswerModel is a DisplayableMixin.
    Responsibility:
    """
    question = models.CharField(
        _('question'),
        max_length=255,

    )
    answer = RichTextField(
        _('answer'),
        config_name='simple',
    )
    sortid = models.IntegerField(
        _('sort'),
        default=0,
        blank=False,
        null=False,
        db_index=True,
        help_text=u'サイトで昇順に並びます',
    )

    class Meta:
        verbose_name = _('Frequently Quetion Answer')
        verbose_name_plural = _('Frequently Quetion Answer')
        ordering = ['sortid', ]

    def __str__(self):
        return self.question



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# frequently_quetion_answer_model.py ends here
