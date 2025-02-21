#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news_category_model_serializer --

"""
from rest_framework import serializers

from publish.models import NewsCategoryModel


class NewsCategoryModelSerializer(serializers.ModelSerializer):
    """NewsCategoryModelSerializer

    NewsCategoryModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """

    class Meta:
        model = NewsCategoryModel
        fields = (
            'name',
            'fgcolor',
            'bgcolor',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_category_model_serializer.py ends here
