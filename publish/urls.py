#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- define urls for messages

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from publish import views


router = DefaultRouter()
router.register(r'activities', views.ActivityModelViewset)
router.register(r'boards', views.BoardModelViewset)
router.register(r'news', views.NewsModelViewset)

urlpatterns = router.urls



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
