#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""garbage_event_model_viewset --

"""
import datetime

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
import django_filters.rest_framework as filters
from rest_framework import filters as rest_filters
from django_filters.rest_framework import DjangoFilterBackend

from home.models.garbage_event_model import GarbageEventModel
from home.serializers.garbage_event_model_serializer import GarbageEventModelSerializer


class GarbageEventModelViewset(viewsets.ModelViewSet):
    """GarbageEventModelViewset

    GarbageEventModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    queryset = GarbageEventModel.objects.all()
    serializer_class = GarbageEventModelSerializer

    def filter_queryset(self, queryset):
        queryset = super(GarbageEventModelViewset, self).filter_queryset(queryset)
        date = self.request.GET.get('date', None)
        if date:
            date_datetime = datetime.datetime.fromisoformat(date)
            queryset = queryset.filter(date=date_datetime)
        limit = self.request.GET.get('limit', '100')
        if limit is not None and limit.isdigit() == True:
            queryset = queryset[:int(limit)]
        return queryset



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# garbage_event_model_viewset.py ends here
