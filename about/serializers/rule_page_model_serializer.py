#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_page_model_serializer --

"""
from rest_framework import serializers

from about.models import RulePageModel


class RulePageModelSerializer(serializers.ModelSerializer):
    """RulePageModelSerializer

    RulePageModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = RulePageModel
        fields = (
            'id',
            'image',
            'sortid',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_page_model_serializer.py ends here
