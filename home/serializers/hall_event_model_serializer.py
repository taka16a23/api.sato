#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_event_model_serializer --

"""
from rest_framework import serializers

from home.models.hall_event_model import HallEventModel


class HallEventModelSerializer(serializers.ModelSerializer):
    """HallEventModelSerializer

    HallEventModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = HallEventModel
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_event_model_serializer.py ends here
