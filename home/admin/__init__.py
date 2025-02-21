#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from home.admin.garbage_event_model_admin import GarbageEventModelAdmin
from home.admin.hall_event_model_admin import HallEventModelAdmin
from home.admin.main_event_model_admin import MainEventModelAdmin
from home.models import GarbageEventModel
from home.models import HallEventModel
from home.models import MainEventModel


__all__ = [
    'GarbageEventModelAdmin',
    'HallEventModelAdmin',
    'MainEventModelAdmin',
]

admin.site.register(GarbageEventModel, GarbageEventModelAdmin)
admin.site.register(HallEventModel, HallEventModelAdmin)
admin.site.register(MainEventModel, MainEventModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
