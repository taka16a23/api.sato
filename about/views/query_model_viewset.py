#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""query_model_viewset --

"""
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend import settings
from about.models import QueryModel
from about.models import QueryReceiverModel
from about.serializers.query_model_serializer import QueryModelSerializer


class QueryModelViewset(viewsets.ModelViewSet):
    """QueryModelViewset

    QueryModelViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]
    http_method_names = ['post', ]
    serializer_class = QueryModelSerializer
    queryset = QueryModel.objects.all()

    def perform_create(self, serializer):
        response = super().perform_create(serializer)
        instance = serializer.instance
        t_subject = _("【{}】お問い合わせ受付".format(settings.SYSTEM_NAME, ))
        t_dicContext = {
            'url': {'scheme': 'https://',
                    'fqdn': settings.URL_SQDN,},
            'id': instance.id,
            'name': instance.name,
            'email_address': instance.email,
            'body': instance.body,
            'system_name': settings.SYSTEM_NAME,
            'company_name': settings.COMPANY_NAME,
            'tel': settings.COMPANY_TEL,
        }
        t_message = render_to_string("about/query_received.txt", t_dicContext)
        send_mail(t_subject, t_message, settings.EMAIL_FROM, [instance.email], fail_silently=True)
        t_message_inner = render_to_string("about/query_received_inner.txt", t_dicContext)
        receiver_models = list(QueryReceiverModel.objects.filter(active=True))
        receiver_emails = [x.email for x in receiver_models]
        send_mail(t_subject, t_message_inner, settings.EMAIL_FROM, receiver_emails, fail_silently=True)
        return response



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# query_model_viewset.py ends here
