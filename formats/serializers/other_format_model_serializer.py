#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""other_format_model_serializer --

"""
from rest_framework import serializers

from formats.models import OtherFormatModel


class OtherFormatModelSerializer(serializers.ModelSerializer):
    """OtherFormatModelSerializer

    OtherFormatModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = OtherFormatModel
        fields = (
            'id',
            'title',
            'description',
            'url',
            'sortid',
            'publish_date',
            'expiry_date',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# other_format_model_serializer.py ends here
