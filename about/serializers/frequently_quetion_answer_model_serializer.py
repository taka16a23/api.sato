#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""frequently_quetion_answer_model_serializer --

"""
from rest_framework import serializers

from about.models import FrequentlyQuetionAnswerModel


class FrequentlyQuetionAnswerModelSerializer(serializers.ModelSerializer):
    """FrequentlyQuetionAnswerModelSerializer

    FrequentlyQuetionAnswerModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = FrequentlyQuetionAnswerModel
        fields = (
            'id',
            'question',
            'answer',
            'sortid',
            'publish_date',
            'expiry_date',
            'status',
            'sortid',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# frequently_quetion_answer_model_serializer.py ends here
