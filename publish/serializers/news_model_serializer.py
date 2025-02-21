#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news_model_serializer --

"""
from rest_framework import serializers

from publish.models.news_model import NewsModel
from publish.serializers.news_category_model_serializer import NewsCategoryModelSerializer


class NewsModelSerializer(serializers.ModelSerializer):
    """NewsModelSerializer

    NewsModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    news_category_display = NewsCategoryModelSerializer(
        source='category',
        read_only=True,
    )

    class Meta:
        model = NewsModel
        fields = (
            'id',
            'title',
            'url',
            'status',
            'news_category_display',
            'publish_date',
            'expiry_date',
            'created_at',
            'modified_at',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_model_serializer.py ends here
