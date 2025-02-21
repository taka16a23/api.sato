#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""security_knowledge_model_viewset --

"""
from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Q

from security.models.security_knowledge_model import SecurityKnowledgeModel
from security.serializers.security_knowledge_model_serializer import SecurityKnowledgeModelSerializer
from base.models.displayable_mixin import DisplayStatusChoices


class SecurityKnowledgeModelViewset(viewsets.ModelViewSet):
    """SecurityKnowledgeModelViewset

    SecurityKnowledgeModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['get', ]
    serializer_class = SecurityKnowledgeModelSerializer

    queryset = SecurityKnowledgeModel.objects.filter(
        status=DisplayStatusChoices.PUBLISHED).filter(
            publish_date__lte=datetime.now()).filter(
                Q(expiry_date__gte=datetime.now())|Q(expiry_date__isnull=True))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# security_knowledge_model_viewset.py ends here
