#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_event_model_viewset --

"""
import datetime

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
import django_filters.rest_framework as filters
from rest_framework import filters as rest_filters
from django_filters.rest_framework import DjangoFilterBackend

from home.models.hall_event_model import HallEventModel
from home.serializers.hall_event_model_serializer import HallEventModelSerializer


class HallEventModelViewset(viewsets.ModelViewSet):
    """HallEventModelViewset

    HallEventModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    queryset = HallEventModel.objects.all()
    serializer_class = HallEventModelSerializer

    def filter_queryset(self, queryset):
        queryset = super(HallEventModelViewset, self).filter_queryset(queryset)
        start = self.request.GET.get('start', None)
        if start:
            start_datetime = datetime.datetime.fromisoformat(start)
            queryset = queryset.filter(start__gte=start_datetime)
        end = self.request.GET.get('end', None)
        if end:
            end_datetime = datetime.datetime.fromisoformat(end)
            queryset = queryset.filter(end__lte=end_datetime)
        limit = self.request.GET.get('limit', '100')
        if limit is not None and limit.isdigit() == True:
            queryset = queryset[:int(limit)]
        return queryset



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_event_model_viewset.py ends here
