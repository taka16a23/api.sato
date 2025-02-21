#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news_model_viewset --

"""
from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Q

from publish.models.news_model import NewsModel
from publish.serializers.news_model_serializer import NewsModelSerializer
from base.models.displayable_mixin import DisplayStatusChoices


class NewsModelViewset(viewsets.ModelViewSet):
    """NewsModelViewset

    NewsModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    queryset = NewsModel.objects.filter(
        status=DisplayStatusChoices.PUBLISHED).filter(
            publish_date__lte=datetime.now()).filter(
                Q(expiry_date__gte=datetime.now())|Q(expiry_date__isnull=True))
    serializer_class = NewsModelSerializer

    def filter_queryset(self, queryset):
        """一覧絞り込みクエリを取得

        最大件数(limit)を拡張
        """
        queryset = super(NewsModelViewset, self).filter_queryset(queryset)
        year = self.request.GET.get('year', None)
        if year is not None and year.isdigit() == True:
            queryset = queryset.filter(publish_date__year=year)
        limit = self.request.GET.get('limit', None)
        if limit is not None and limit.isdigit() == True:
            queryset = queryset[:int(limit)]
        return queryset



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_model_viewset.py ends here
