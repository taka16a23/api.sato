#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""emergency_view --

"""
import requests

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from lxml import html
from lxml.cssselect import CSSSelector


class EmergencyView(APIView):
    """EmergencyView

    EmergencyView is a APIView.
    Responsibility:
    """
    permission_classes = (
        permissions.AllowAny,
    )

    NAME_SELECTOR = CSSSelector('.name')

    HASANNOUNCED_SELECTOR = CSSSelector('.hasAnnounced')

    NAME_MAP = {
        '本部体制設置': 'honbutaisei',
        '避難情報': 'hinanjouhou',
        '避難所情報': 'hinanjojouhou',
        '国民保護情報': 'kokuminhogojouhou',
    }

    def get(self, request, format=None):
        data = {}
        res = requests.get('https://dis-shiga.jp/pc/topdis-shiga.html')
        if not res.ok:
            return JsonResponse([data], safe=False)
        soup = html.fromstring(res.text)
        emergencies = soup.xpath('//*[@class="emergencyInfoBox"]/div/h2')

        names = self.NAME_MAP.keys()

        for emergency in emergencies:
            name_elt = self.NAME_SELECTOR(emergency)
            if len(name_elt) < 1:
                continue
            for key_name in names:
                if key_name in name_elt[0].text:
                    data[self.NAME_MAP[key_name]] = bool(self.HASANNOUNCED_SELECTOR(emergency))

        return JsonResponse([data], safe=False, json_dumps_params={'ensure_ascii': False})



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# emergency_view.py ends here
