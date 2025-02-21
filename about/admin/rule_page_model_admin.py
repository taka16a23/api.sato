#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_page_model_admin --

"""
from django.contrib import admin


class RulePageModelAdmin(admin.ModelAdmin):
    """RulePageModelAdmin

    RulePageModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'book',
        'image',
        'sortid',
    )
    list_editable = (
        'sortid',
    )
    ordering = (
        '-sortid',
    )
    fieldsets = (
        (None, {
            'fields': ['book', 'image', 'sortid'],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_page_model_admin.py ends here
