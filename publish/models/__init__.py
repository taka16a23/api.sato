#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from publish.models.activity_model import ActivityModel
from publish.models.board_model import BoardModel
from publish.models.news_category_model import NewsCategoryModel
from publish.models.news_model import NewsModel

__all__ = [
    'ActivityModel',
    'BoardModel',
    'NewsCategoryModel',
    'NewsModel',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
