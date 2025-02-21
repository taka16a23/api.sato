#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board_model_viewset --

"""
from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
import django_filters.rest_framework as filters
from rest_framework import filters as rest_filters
from django_filters.rest_framework import DjangoFilterBackend

from publish.models.board_model import BoardModel
from publish.serializers.board_model_serializer import BoardModelSerializer
from base.models.displayable_mixin import DisplayStatusChoices


class BoardModelViewset(viewsets.ModelViewSet):
    """BoardModelViewset

    BoardModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    queryset = BoardModel.objects.filter(
        status=DisplayStatusChoices.PUBLISHED).filter(
            publish_date__lte=datetime.now()).filter(
                Q(expiry_date__gte=datetime.now())|Q(expiry_date__isnull=True))
    serializer_class = BoardModelSerializer

    def filter_queryset(self, queryset):
        """一覧絞り込みクエリを取得

        公開年指定(year)
        """
        queryset = super(BoardModelViewset, self).filter_queryset(queryset)
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
# board_model_viewset.py ends here
