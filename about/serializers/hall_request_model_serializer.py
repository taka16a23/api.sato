#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_request_model_serializer --

"""
from rest_framework import serializers

from about.models import HallRequestModel


class HallRequestModelSerializer(serializers.ModelSerializer):
    """HallRequestModelSerializer

    HallRequestModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """

    class Meta:
        model = HallRequestModel
        fields = (
            'group_name',
            'responsible_person',
            'address',
            'phone_number',
            'email_address',
            'reason',
            'start_datetime',
            'end_datetime',
            'room',
            'detail',
            'note',
            'is_finished',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_request_model_serializer.py ends here
