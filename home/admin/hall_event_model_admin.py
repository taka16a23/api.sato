#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""hall_event_model_admin --

"""
from django.contrib import admin


class HallEventModelAdmin(admin.ModelAdmin):
    """HallEventModelAdmin

    HallEventModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'gid',
        'summary',
        'description',
        'date',
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
# hall_event_model_admin.py ends here
