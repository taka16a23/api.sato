#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""frequently_quetion_answer_model_viewset --

"""
from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Q

from about.models import FrequentlyQuetionAnswerModel
from about.serializers.frequently_quetion_answer_model_serializer import FrequentlyQuetionAnswerModelSerializer
from base.models.displayable_mixin import DisplayStatusChoices


class FrequentlyQuetionAnswerModelViewset(viewsets.ModelViewSet):
    """FrequentlyQuetionAnswerModelViewset

    FrequentlyQuetionAnswerModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    serializer_class = FrequentlyQuetionAnswerModelSerializer

    queryset = FrequentlyQuetionAnswerModel.objects.filter(
        status=DisplayStatusChoices.PUBLISHED).filter(
            publish_date__lte=datetime.now()).filter(
                Q(expiry_date__gte=datetime.now())|Q(expiry_date__isnull=True))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# frequently_quetion_answer_model_viewset.py ends here
