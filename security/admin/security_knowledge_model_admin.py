#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""security_knowledge_model_admin --

"""
from django.contrib import admin


class SecurityKnowledgeModelAdmin(admin.ModelAdmin):
    """SecurityKnowledgeModelAdmin

    SecurityKnowledgeModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'title',
        'publish_date',
        'expiry_date',
        'status',
    )
    list_editable = (
        'status',
    )
    exclude = [
        'sortid',
    ]
    fieldsets = (
        (None, {
            'fields': ['title', 'thumbnail', 'url', 'description', ('publish_date', 'expiry_date'), 'status', ],
        }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# security_knowledge_model_admin.py ends here
