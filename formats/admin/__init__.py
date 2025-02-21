#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from formats.models import SatoFormatModel
from formats.models import OtherFormatModel
from formats.admin.sato_format_model_admin import SatoFormatModelAdmin
from formats.admin.other_format_model_admin import OtherFormatModelAdmin

__all__ = [
    'SatoFormatModelAdmin',
    'OtherFormatModelAdmin',
]

admin.site.register(SatoFormatModel, SatoFormatModelAdmin)
admin.site.register(OtherFormatModel, OtherFormatModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
