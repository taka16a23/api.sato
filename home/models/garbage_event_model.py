#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""garbage_event_model --

"""
import urllib

from django.db import models

from backend.settings import STATIC_URL


GARBAGE_IMGS = {u'紙ごみ': urllib.parse.urljoin(STATIC_URL, 'images/paper.jpg'),
                u'燃やせるごみ': urllib.parse.urljoin(STATIC_URL, 'images/combustibles.jpg'),
                u'透明びん、茶色びん': urllib.parse.urljoin(STATIC_URL, 'images/bottles.jpg'),
                u'プラ容器包装': urllib.parse.urljoin(STATIC_URL, 'images/plastics.jpg'),
                u'ペットボトル': urllib.parse.urljoin(STATIC_URL, 'images/PET.jpg'),
                u'燃やせないごみ': urllib.parse.urljoin(STATIC_URL, 'images/incombustibles.jpg'),
                u'かん': urllib.parse.urljoin(STATIC_URL, 'images/cans.jpg'),
}

EVENT_CONFIRMED_STATUS = 1
EVENT_TENTATIVE_STATUS = 2
EVENT_CANCELLED_STATUS = 3

EVENT_STATUS = ((EVENT_CONFIRMED_STATUS, 'confirmed'),
                (EVENT_TENTATIVE_STATUS, 'tentative'),
                (EVENT_CANCELLED_STATUS, 'cancelled'), )


class GarbageEventModel(models.Model):
    """GarbageEventModel

    GarbageEventModel is a models.Model.
    Responsibility:
    """
    gid = models.TextField()
    summary = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )
    date = models.DateField(
        null=True,
        blank=True,
    )
    url = models.URLField(
        null=True,
        blank=True,
    )
    status = models.IntegerField(
        choices=EVENT_STATUS,
        default=EVENT_CONFIRMED_STATUS,
    )

    def __str__(self):
        return self.summary

    def url_of_image(self, ):
        return GARBAGE_IMGS.get(self.summary, '')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# garbage_event_model.py ends here
