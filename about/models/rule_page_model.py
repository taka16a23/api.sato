#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_page_model --

"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from about.models.rule_book_model import RuleBookModel


class RulePageModel(models.Model):
    """RulePageModel

    RulePageModel is a models.Model.
    Responsibility:
    """
    book = models.ForeignKey(
        RuleBookModel,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        _('Page Image'),
        upload_to='rulepage/',
        blank=False,
        null=False,
    )
    sortid = models.IntegerField(
        ' ',
        default=0,
        blank=False,
        null=False,
        db_index=True,
        help_text=u'サイトで昇順に並びます',
    )

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()

    class Meta(object):
        verbose_name = _('Rule page')
        verbose_name_plural = _('Rule page')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_page_model.py ends here
