#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sato_format_model_admin --

"""
from django.contrib import admin


class SatoFormatModelAdmin(admin.ModelAdmin):
    """SatoFormatModelAdmin

    SatoFormatModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'title',
        'publish_date',
        'expiry_date',
        'status',
    )
    list_editable = (
        'status',
    )
    exclude = [
        'sortid',
    ]
    fieldsets = (
        (None, {
            'fields': ['title', 'description', 'file', 'form', ('publish_date', 'expiry_date'), 'status', ],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sato_format_model_admin.py ends here
