#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""query_model_admin --

"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class QueryModelAdmin(admin.ModelAdmin):
    """QueryModelAdmin

    QueryModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'query_id',
        'status',
        'requested_at',
        'name',
        'email',
        'body',
    )
    list_editable = (
    )
    ordering = (
        '-created_at',
    )

    def query_id(self, obj):
        return obj.id

    query_id.short_description = _('query id')

    def requested_at(self, obj):
        return obj.created_at

    requested_at.short_description = _('requested at')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# query_model_admin.py ends here
