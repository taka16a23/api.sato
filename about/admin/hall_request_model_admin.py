#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_request_model_admin --

"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class HallRequestModelAdmin(admin.ModelAdmin):
    """HallRequestModelAdmin

    HallRequestModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'hall_request_id',
        'is_finished',
        'requested_at',
        'group_name',
        'responsible_person',
        'address',
        'phone_number',
        'room',
        'email_address',
        'start_datetime',
        'end_datetime',
        'reason',
    )
    list_editable = (
    )
    ordering = (
        '-created_at',
    )

    def hall_request_id(self, obj):
        return obj.id

    hall_request_id.short_description = _('hall request id')

    def requested_at(self, obj):
        return obj.created_at
    requested_at.short_description = _('requested at')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_request_model_admin.py ends here
