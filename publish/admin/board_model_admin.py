#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board_model_admin --

"""
from django.contrib import admin


class BoardModelAdmin(admin.ModelAdmin):
    """BoardModelAdmin

    BoardModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'title',
        'status',
        'publish_date',
        'expiry_date',
    )
    list_editable = (
        'status',
    )
    ordering = (
        '-publish_date',
    )
    radio_fields = {
        'status': admin.HORIZONTAL,
    }
    fieldsets = (
        (None, {
            'fields': ['title', 'file', 'status'],

        }),
        (u'公開日/有効期限の設定',
         {'classes': ('collapse', ),
          'fields': [('publish_date', 'expiry_date'), ],}),
        (u'サムネイル',
         {'classes': ('collapse', ),
          'fields': ['thumbnail', ],}),
        (u'お知らせ',
         {'classes': ('collapse', ),
          'fields': ['news', ],}),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# board_model_admin.py ends here
