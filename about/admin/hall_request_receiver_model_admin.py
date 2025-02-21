#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_request_receiver_model_admin --

"""
from django.contrib import admin


class HallRequestReceiverModelAdmin(admin.ModelAdmin):
    """HallRequestReceiverModelAdmin

    HallRequestReceiverModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'name',
        'email',
        'active',
    )
    list_editable = (
        'active',
    )
    ordering = (
        'name',
    )
    exclude = (
        'created_by',
        'modified_by',
    )
    fieldsets = (
        (None, {
            'fields': ['name', 'email', 'active'],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hall_request_receiver_model_admin.py ends here
