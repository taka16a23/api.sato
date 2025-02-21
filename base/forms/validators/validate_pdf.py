#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""pdf_validator --

"""
from django.forms import forms


def validate_pdf(value):
    if not hasattr(value.file, 'content_type'):
        return
    if value.file.content_type != 'application/pdf':
        raise forms.ValidationError(u'PDF ではありません。PDF ファイルを選択してください。')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pdf_validator.py ends here
