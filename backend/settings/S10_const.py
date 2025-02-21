#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S10_const --

"""
from urllib import parse as urlparse


# Do not change here. change at 90_local.py.
DEBUG = True

URL_SQDN = "satojichi.ddns.net"

SYSTEM_NAME = "里自治会ホームページ"

COMPANY_NAME = "里自治会"

COMPANY_TEL = "077-546-6905"

COMPANY_FAX = "077-546-6905"

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


class EventStatus(object):
    """EventStatus

    EventStatus is a object.
    Responsibility:
    """
    CONFIRMED = 1
    TENTATIVE = 2
    CANCELLED = 3

    @staticmethod
    def as_tuple(cls, ):
        """SUMMARY

        as_tuple()

        @Return:

        @Error:
        """
        return (
            (EventStatus.CONFIRMED, 'confirmed'),
            (EventStatus.TENTATIVE, 'tentative'),
            (EventStatus.CANCELLED, 'cancelled'),
        )

    @staticmethod
    def as_dict(cls, ):
        """SUMMARY

        as_dict()

        @Return:

        @Error:
        """
        return {x[1]: x[0] for x in EventStatus.as_tuple()}


GARBAGE_IMGS = {
    u'紙ごみ': urlparse.urljoin(STATIC_URL, 'images/paper.jpg'),
    u'燃やせるごみ': urlparse.urljoin(STATIC_URL, 'images/combustibles.jpg'),
    u'透明びん、茶色びん': urlparse.urljoin(STATIC_URL, 'images/bottles.jpg'),
    u'プラ容器包装': urlparse.urljoin(STATIC_URL, 'images/plastics.jpg'),
    u'ペットボトル': urlparse.urljoin(STATIC_URL, 'images/PET.jpg'),
    u'燃やせないごみ': urlparse.urljoin(STATIC_URL, 'images/incombustibles.jpg'),
    u'かん': urlparse.urljoin(STATIC_URL, 'images/cans.jpg'),
}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S10_const.py ends here
