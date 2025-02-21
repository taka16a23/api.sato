#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""displayable_manager --

"""
import datetime

from django.db.models.query import QuerySet

from base.base_manager import BaseManager
from base.models.displayable_mixin import DisplayStatusChoices


class DisplayableManager(BaseManager):
    """DisplayableManager

    DisplayableManager is a BaseManager.
    Responsibility:
    """
    class DisplayableQuerySet(QuerySet):
        """DisplayableQuerySet

        DisplayableQuerySet is a QuerySet.
        Responsibility:
        """
        def published(self, a_date=None):
            """本日まで公開中ステータスかつ有効期限内一覧クエリセットを取得

            @Arguments:
            - `a_date`: (datetime) 指定日時

            @Return:

            published()

            @Error:
            """
            t_date = a_date
            if t_date is None:
                t_date = datetime.datetime.now()
            return self.filter(
                Q(publish_date__lte=t_date)|Q(publish_date__isnull=True),
                Q(expiry_date__gte=t_date)|Q(expiry_date__isnull=True),
                Q(status=DisplayStatusChoices.PUBLISHED),
            )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# displayable_manager.py ends here
