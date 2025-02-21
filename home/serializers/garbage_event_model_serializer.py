#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""garbage_event_model_serializer --

"""
import urllib
from rest_framework import serializers

from backend.settings import STATIC_URL
from home.models.garbage_event_model import GarbageEventModel


GARBAGE_IMGS = {u'紙ごみ': urllib.parse.urljoin(STATIC_URL, 'images/paper.jpg'),
                u'燃やせるごみ': urllib.parse.urljoin(STATIC_URL, 'images/combustibles.jpg'),
                u'透明びん、茶色びん': urllib.parse.urljoin(STATIC_URL, 'images/bottles.jpg'),
                u'プラ容器包装': urllib.parse.urljoin(STATIC_URL, 'images/plastics.jpg'),
                u'ペットボトル': urllib.parse.urljoin(STATIC_URL, 'images/PET.jpg'),
                u'燃やせないごみ': urllib.parse.urljoin(STATIC_URL, 'images/incombustibles.jpg'),
                u'かん': urllib.parse.urljoin(STATIC_URL, 'images/cans.jpg'),
}


class GarbageEventModelSerializer(serializers.ModelSerializer):
    """GarbageEventModelSerializer

    GarbageEventModelSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    url_of_image = serializers.SerializerMethodField()

    class Meta:
        model = GarbageEventModel
        fields = (
            'gid',
            'summary',
            'date',
            'url',
            'status',
            'url_of_image',
        )

    def url_of_image(self, obj):
        return GARBAGE_IMGS.get(obj.summary, '')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# garbage_event_model_serializer.py ends here
