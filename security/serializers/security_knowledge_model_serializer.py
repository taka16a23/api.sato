#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""security_knowledge_model_serializer --

"""
from rest_framework import serializers

from security.models.security_knowledge_model import SecurityKnowledgeModel


class SecurityKnowledgeModelSerializer(serializers.ModelSerializer):
    """SecurityKnowledgeModelSerializer

    SecurityKnowledgeModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """

    class Meta:
        model = SecurityKnowledgeModel
        fields = (
            'id',
            'title',
            'description',
            'url',
            'thumbnail',
            'sortid',
            'publish_date',
            'expiry_date',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# security_knowledge_model_serializer.py ends here
