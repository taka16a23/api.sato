#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from publish.views.activity_model_viewset import ActivityModelViewset
from publish.views.board_model_viewset import BoardModelViewset
from publish.views.news_model_viewset import NewsModelViewset

__all__ = [
    'ActivityModelViewset',
    'BoardModelViewset',
    'NewsModelViewset',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
