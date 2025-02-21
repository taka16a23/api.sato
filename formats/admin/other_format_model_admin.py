#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""other_format_model_admin --

"""
from django.contrib import admin


class OtherFormatModelAdmin(admin.ModelAdmin):
    """OtherFormatModelAdmin

    OtherFormatModelAdmin is a admin.ModelAdmin.
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
            'fields': ['title', 'description', 'url', ('publish_date', 'expiry_date'), 'status', ],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# other_format_model_admin.py ends here
