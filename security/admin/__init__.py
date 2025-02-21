#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from security.models import SecurityKnowledgeModel
from security.admin.security_knowledge_model_admin import SecurityKnowledgeModelAdmin

__all__ = [
    'SecurityKnowledgeModelAdmin',
]

admin.site.register(SecurityKnowledgeModel, SecurityKnowledgeModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
