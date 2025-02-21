#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_book_model_viewset --

"""
from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Q

from about.models import RuleBookModel
from about.serializers.rule_book_model_serializer import RuleBookModelSerializer
from base.models.displayable_mixin import DisplayStatusChoices


class RuleBookModelViewset(viewsets.ModelViewSet):
    """RuleBookModelViewset

    RuleBookModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    serializer_class = RuleBookModelSerializer

    queryset = RuleBookModel.objects.filter(
        status=DisplayStatusChoices.PUBLISHED).filter(
            publish_date__lte=datetime.now()).filter(
                Q(expiry_date__gte=datetime.now())|Q(expiry_date__isnull=True))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_book_model_viewset.py ends here
