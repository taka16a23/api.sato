#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news_model_admin --

"""
from django.contrib import admin


class NewsModelAdmin(admin.ModelAdmin):
    """NewsModelAdmin

    NewsModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'title',
        'category',
        'status',
        'publish_date',
        'expiry_date',
    )
    list_editable = (
        'category',
        'status',
    )
    ordering = (
        '-modified_at',
    )
    radio_fields = {
        'status': admin.HORIZONTAL,
    }
    fieldsets = (
        (None, {
            'fields': ['title', 'url',  'category', ('publish_date', 'expiry_date'), 'status'],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_model_admin.py ends here
