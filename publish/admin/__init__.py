#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from publish.admin.activity_model_admin import ActivityModelAdmin
from publish.admin.board_model_admin import BoardModelAdmin
from publish.admin.news_category_model_admin import NewsCategoreyModelAdmin
from publish.admin.news_model_admin import NewsModelAdmin
from publish.models import ActivityModel
from publish.models import BoardModel
from publish.models import NewsCategoryModel
from publish.models import NewsModel


__all__ = [
    'ActivityModelAdmin',
    'BoardModelAdmin',
    'NewsCategoreyModelAdmin',
    'NewsModelAdmin',
]

admin.site.register(ActivityModel, ActivityModelAdmin)
admin.site.register(BoardModel, BoardModelAdmin)
admin.site.register(NewsCategoryModel, NewsCategoreyModelAdmin)
admin.site.register(NewsModel, NewsModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
