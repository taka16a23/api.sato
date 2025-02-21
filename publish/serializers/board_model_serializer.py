#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board_model_serializer --

"""
from rest_framework import serializers

from publish.models.board_model import BoardModel


class BoardModelSerializer(serializers.ModelSerializer):
    """BoardModelSerializer

    BoardModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """

    class Meta:
        model = BoardModel
        fields = (
            'id',
            'title',
            'file',
            'thumbnail',
            'publish_date',
            'expiry_date',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# board_model_serializer.py ends here
