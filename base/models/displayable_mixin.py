#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""displayable_mixin --

"""
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_stamp_mixin import BaseStampMixin
from base.helpers import base_concrete_model


class DisplayStatusChoices(models.TextChoices):
    DRAFT = "1", _("draft")
    PUBLISHED = "2", _("publish")


class DisplayableMixin(BaseStampMixin):
    """DisplayableMixin

    DisplayableMixin is a BaseStampMixin.
    Responsibility:
    """
    class Meta:
        abstract = True

    # ステータス
    status = models.CharField(
        _('status'),
        max_length=1,
        choices=DisplayStatusChoices,
        default=DisplayStatusChoices.DRAFT,
        help_text=_('下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。'),
    )

    # 公開日時
    publish_date = models.DateTimeField(
        _('publish date'),
        blank=True,
        null=True,
        db_index=True,
        help_text=u'公開を選択すると、ここで設定した日時までは公開されません')

    # 有効期限
    expiry_date = models.DateTimeField(
        _('expiry date'),
        blank=True,
        null=True,
        help_text=_('公開を選択すると、ここで設定した日時以降は公開されません'),
    )

    def next_publish_date(self, ):
        concrete_model = base_concrete_model(DisplayableMixin, self)
        nexts = concrete_model.objects.published().filter(
            publish_date__gt=self.publish_date).order_by('publish_date')
        if nexts:
            return nexts[0]
        return False

    def previous_publish_date(self, ):
        concrete_model = base_concrete_model(DisplayableMixin, self)
        prevs = concrete_model.objects.published().filter(
            publish_date__lt=self.publish_date).order_by('-publish_date')
        if prevs:
            return prevs[0]
        return False

    def save(self, **kwargs):
        if self.publish_date is None:
            self.publish_date = datetime.datetime.now()
        super(DisplayableMixin, self).save(**kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# displayable_mixin.py ends here
