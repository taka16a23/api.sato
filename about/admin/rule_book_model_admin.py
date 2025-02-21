#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_book_model_admin --

"""
from django.contrib import admin


class RuleBookModelAdmin(admin.ModelAdmin):
    """RuleBookModelAdmin

    RuleBookModelAdmin is a admin.ModelAdmin.
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
        '-sortid',
    )
    radio_fields = {
        'status': admin.HORIZONTAL,
    }
    fieldsets = (
        (None, {
            'fields': ['title', 'document',  ('publish_date', 'expiry_date'), 'status'],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_book_model_admin.py ends here
