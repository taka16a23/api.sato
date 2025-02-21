#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- define urls for messages

"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from about import views


router = DefaultRouter()
router.register(r'rules', views.RuleBookModelViewset)
router.register(r'hall/request', views.HallRequestModelViewset)
router.register(r'faq', views.FrequentlyQuetionAnswerModelViewset)
router.register(r'query', views.QueryModelViewset)

urlpatterns = router.urls



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
