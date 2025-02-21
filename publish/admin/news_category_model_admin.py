#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news_category_model_admin --

"""
from django.contrib import admin


class NewsCategoreyModelAdmin(admin.ModelAdmin):
    """NewsCategoreyModelAdmin

    NewsCategoreyModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'name',
        'fgcolor',
        'bgcolor',
    )
    list_editable = (
        'fgcolor',
        'bgcolor',
    )
    exclude = ['sortid', ]

    def get_actions(self, request):
        actions = super(NewsCategoreyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news_category_model_admin.py ends here
