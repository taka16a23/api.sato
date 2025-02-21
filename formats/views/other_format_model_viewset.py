#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""other_format_model_viewset --

"""
from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Q

from formats.models import OtherFormatModel
from formats.serializers.other_format_model_serializer import OtherFormatModelSerializer
from base.models.displayable_mixin import DisplayStatusChoices


class OtherFormatModelViewset(viewsets.ModelViewSet):
    """OtherFormatModelViewset

    OtherFormatModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    serializer_class = OtherFormatModelSerializer

    queryset = OtherFormatModel.objects.filter(
        status=DisplayStatusChoices.PUBLISHED).filter(
            publish_date__lte=datetime.now()).filter(
                Q(expiry_date__gte=datetime.now())|Q(expiry_date__isnull=True))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# other_format_model_viewset.py ends here
