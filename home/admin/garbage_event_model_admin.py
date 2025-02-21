#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""garbage_event_model_admin --

"""
from django.contrib import admin


class GarbageEventModelAdmin(admin.ModelAdmin):
    """GarbageEventModelAdmin

    GarbageEventModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'gid',
        'summary',
        'date',
        'url',
        'status',
    )
    ordering = (
        '-date',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# garbage_event_model_admin.py ends here
