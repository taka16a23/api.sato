#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""main_event_model_admin --

"""
from django.contrib import admin


class MainEventModelAdmin(admin.ModelAdmin):
    """MainEventModelAdmin

    MainEventModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'gid',
        'summary',
        'description',
        'url',
        'status',
        'start',
        'end',
        'created',
        'modified',
    )
    ordering = (
        '-start',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# main_event_model_admin.py ends here
