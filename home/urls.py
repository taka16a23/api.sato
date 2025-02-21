#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- define urls for messages

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home import views


router = DefaultRouter()
router.register(r'halls', views.HallEventModelViewset)
router.register(r'main', views.MainEventModelViewset)
router.register(r'garbages', views.GarbageEventModelViewset)

urlpatterns = router.urls



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
