#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""query_model_serializer --

"""
from rest_framework import serializers

from about.models import QueryModel


class QueryModelSerializer(serializers.ModelSerializer):
    """QueryModelSerializer

    QueryModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """

    class Meta:
        model = QueryModel
        fields = (
            'id',
            'name',
            'email',
            'body',
            'status',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# query_model_serializer.py ends here
