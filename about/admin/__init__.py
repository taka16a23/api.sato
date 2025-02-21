#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from about.admin.frequently_quetion_answer_model_admin import FrequentlyQuetionAnswerModelAdmin
from about.admin.hall_request_model_admin import HallRequestModelAdmin
from about.admin.hall_request_receiver_model_admin import HallRequestReceiverModelAdmin
from about.admin.query_model_admin import QueryModelAdmin
from about.admin.query_receiver_model_admin import QueryReceiverModelAdmin
from about.admin.rule_book_model_admin import RuleBookModelAdmin
from about.admin.rule_page_model_admin import RulePageModelAdmin
from about.models import FrequentlyQuetionAnswerModel
from about.models import HallRequestModel
from about.models import HallRequestReceiverModel
from about.models import QueryModel
from about.models import QueryReceiverModel
from about.models import RuleBookModel
from about.models import RulePageModel

__all__ = [
    'FrequentlyQuetionAnswerModelAdmin',
    'HallRequestModelAdmin',
    'HallRequestReceiverModelAdmin',
    'QueryModelAdmin',
    'QueryReceiverModelAdmin',
    'RuleBookModelAdmin',
    'RulePageModelAdmin',
]

admin.site.register(FrequentlyQuetionAnswerModel, FrequentlyQuetionAnswerModelAdmin)
admin.site.register(HallRequestModel, HallRequestModelAdmin)
admin.site.register(HallRequestReceiverModel, HallRequestReceiverModelAdmin)
admin.site.register(QueryModel, QueryModelAdmin)
admin.site.register(QueryReceiverModel, QueryReceiverModelAdmin)
admin.site.register(RuleBookModel, RuleBookModelAdmin)
admin.site.register(RulePageModel, RulePageModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
