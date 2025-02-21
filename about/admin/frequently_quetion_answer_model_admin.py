#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""frequently_quetion_answer_model_admin --

"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class FrequentlyQuetionAnswerModelAdmin(admin.ModelAdmin):
    """FrequentlyQuetionAnswerModelAdmin

    FrequentlyQuetionAnswerModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'question',
        'answer',
        'sortid',
        'publish_date',
        'expiry_date',
        'status',
    )
    list_editable = (
        'sortid',
    )
    ordering = (
        'sortid',
    )
    fieldsets = (
        (None, {
            'fields': ['question', 'answer', 'sortid', ('publish_date', 'expiry_date'), 'status', ],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# frequently_quetion_answer_model_admin.py ends here
