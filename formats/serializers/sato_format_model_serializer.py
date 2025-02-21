#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sato_format_model_serializer --

"""
from rest_framework import serializers

from formats.models import SatoFormatModel


class SatoFormatModelSerializer(serializers.ModelSerializer):
    """SatoFormatModelSerializer

    SatoFormatModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = SatoFormatModel
        fields = (
            'id',
            'title',
            'description',
            'file',
            'form',
            'sortid',
            'publish_date',
            'expiry_date',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sato_format_model_serializer.py ends here
