#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""main_event_model_serializer --

"""
from rest_framework import serializers

from home.models.main_event_model import MainEventModel


class MainEventModelSerializer(serializers.ModelSerializer):
    """MainEventModelSerializer

    MainEventModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = MainEventModel
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# main_event_model_serializer.py ends here
