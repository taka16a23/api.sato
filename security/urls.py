#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- define urls for messages

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from security import views
from security.views.weather_warnings_view import WeatherWarningsView
from security.views.emergency_view import EmergencyView


router = DefaultRouter()
router.register(r'knowledge', views.SecurityKnowledgeModelViewset)

urlpatterns = router.urls
urlpatterns.append(path('weather_warnings/', WeatherWarningsView.as_view()))
urlpatterns.append(path('emergencies/', EmergencyView.as_view()))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
