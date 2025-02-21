#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_receive_model_viewset --

"""
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend import settings
from about.models import HallRequestModel
from about.models import HallRequestReceiverModel
from about.serializers.hall_request_model_serializer import HallRequestModelSerializer


class HallRequestModelViewset(viewsets.ModelViewSet):
    """HallRequestModelViewset

    HallRequestModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['post', ]
    serializer_class = HallRequestModelSerializer
    queryset = HallRequestModel.objects.all()

    def perform_create(self, serializer):
        response = super().perform_create(serializer)
        instance = serializer.instance
        t_subject = _("【{}】公民館申込み受付".format(settings.SYSTEM_NAME, ))
        t_dicContext = {
            'url': {'scheme': 'https://',
                    'fqdn': settings.URL_SQDN,},
            'id': instance.id,
            'group_name': instance.group_name,
            'address': instance.address,
            'phone_number': instance.phone_number,
            'responsible_person': instance.responsible_person,
            'email_address': instance.email_address,
            'reason': instance.reason,
            'start_datetime': instance.start_datetime,
            'end_datetime': instance.end_datetime.strftime('%H:%M'),
            'room': instance.room,
            'detail': instance.detail,
            'note': instance.note,
            'system_name': settings.SYSTEM_NAME,
            'company_name': settings.COMPANY_NAME,
            'tel': settings.COMPANY_TEL,
        }
        t_message = render_to_string("about/hall_request_received.txt", t_dicContext)
        send_mail(t_subject, t_message, settings.EMAIL_FROM, [instance.email_address], fail_silently=True)
        t_message_inner = render_to_string("about/hall_request_received_inner.txt", t_dicContext)
        receiver_models = list(HallRequestReceiverModel.objects.filter(active=True))
        receiver_emails = [x.email for x in receiver_models]
        send_mail(t_subject, t_message_inner, settings.EMAIL_FROM, receiver_emails, fail_silently=True)
        return response



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_receive_model_viewset.py ends here
