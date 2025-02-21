#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from about.views.frequently_quetion_answer_model_viewset import FrequentlyQuetionAnswerModelViewset
from about.views.hall_receive_model_viewset import HallRequestModelViewset
from about.views.query_model_viewset import QueryModelViewset
from about.views.rule_book_model_viewset import RuleBookModelViewset

__all__ = [
    'FrequentlyQuetionAnswerModelViewset',
    'HallRequestModelViewset',
    'QueryModelViewset',
    'RuleBookModelViewset',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
