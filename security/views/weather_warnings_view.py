#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""weather_warnings_view --

"""
import requests
from collections import namedtuple

from lxml import html
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions


class WeatherWarningsView(APIView):

    permission_classes = (
        permissions.AllowAny,
    )

    WEATHER_WARNINGS = (
        # Em = Emergency
        'Em_Snow_storm',         # 暴風雪特別警報
        'Em_Landslide_disaster', # 土砂災害特別警報
        'Em_Flood_damage',       # 浸水害特別警報
        'Em_Storm',              # 暴風特別警報
        'Em_Heavy_snow',         # 大雪特別警報
        # Wa = Warning
        'Wa_Snow_storm',         # 暴風雪警報
        'Wa_Landslide_disaster', # 土砂災害警報
        'Wa_Flood_damage',       # 浸水害警報
        'Wa_Flood',              # 洪水警報
        'Wa_Storm',              # 暴風警報
        'Wa_Heavy_snow',         # 大雪警報
        # Ad = Advisory
        'Ad_Heavy_rain',         # 大雨注意報
        'Ad_Heavy_snow',         # 大雪注意報
        'Ad_Gale_and_snow',      # 風雪注意報
        'Ad_Thunderstorm',       # 雷注意報
        'Ad_Gale',               # 強風注意報
        'Ad_Snow_melting',       # 融雪注意報
        'Ad_Flood',              # 洪水注意報
        'Ad_Dense_fog',          # 濃霧注意報
        'Ad_Dry_air',            # 乾燥注意報
        'Ad_Avalanche',          # なだれ注意報
        'Ad_Low_temperature',    # 低温注意報
        'Ad_Frost',              # 霜注意報
        'Ad_Ice_accretion',      # 着氷注意報
        'Ad_Snow_accretion',     # 着雪注意報
    )

    def get(self, request, format=None):
        data = {}
        res = requests.get('http://shiga-bousai.jp/announce/weather.php')
        if not res.ok:
            return JsonResponse([data], safe=False)
        soup = html.fromstring(res.text)
        # 記録的短時間大雨情報
        tds =  soup.xpath("//td")
        for td in tds:
            if 'class' in td.attrib and 'ooameBody' in td.attrib['class']:
                data['heavyRainWarning'] = tds[0].text
        th_list = soup.xpath('//*[@id="mainContentsContainer"]/table[1]/tr/th')
        tr = None
        for th in th_list:
            if '大津市南部' == th.text:
                tr = th.getparent()
                break
        data['date'] = soup.xpath(
            '//*[@id="mainTitleContainer"]/font')[0].text.replace(u'　', '')
        if tr is None:
            return JsonResponse([data], safe=False, json_dumps_params={'ensure_ascii': False})
        td_list = tr.xpath('td')

        for name, value in zip(self.WEATHER_WARNINGS, td_list):
            data[name] = value.text
        return JsonResponse([data], safe=False, json_dumps_params={'ensure_ascii': False})



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# weather_warnings_view.py ends here
