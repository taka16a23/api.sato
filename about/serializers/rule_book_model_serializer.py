#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_book_model_serializer --

"""
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from about.models import RuleBookModel, RulePageModel
from about.serializers.rule_page_model_serializer import RulePageModelSerializer


class RuleBookModelSerializer(serializers.ModelSerializer):
    """RuleBookModelSerializer

    RuleBookModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    images = SerializerMethodField()

    class Meta:
        model = RuleBookModel
        fields = (
            'id',
            'title',
            'document',
            'sortid',
            'images',
        )

    def get_images(self, obj):
        """画像一覧を取得"""
        images = RulePageModelSerializer(
            RulePageModel.objects.all().filter(
                book = RuleBookModel.objects.get(id=obj.id)), many=True).data
        return images



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_book_model_serializer.py ends here
