#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rule_book_model --

"""
import tempfile
import pathlib
from time import sleep

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.files import File
from pdf2image import convert_from_path

from base.models.displayable_mixin import DisplayableMixin


class RuleBookModel(DisplayableMixin):
    """RuleBookModel

    RuleBookModel is a DisplayableMixin.
    Responsibility:
    """
    title = models.CharField(
        _('title'),
        max_length=255,
        null=False,
        blank=False,
    )
    document = models.FileField(
        _('PDF'),
        upload_to='rule',
        null=False,
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
    )
    sortid = models.IntegerField(
        u' ',
        default=0,
        blank=False,
        null=False,
        db_index=True,
        help_text=u'サイトで昇順に並びます',
    )

    def save(self, *args, **kwargs):
        from about.models.rule_page_model import RulePageModel
        super(RuleBookModel, self).save(*args, **kwargs)
        RulePageModel.objects.filter(book=self).delete()
        pages = convert_from_path(self.document.path)
        with tempfile.TemporaryDirectory() as tempdirectory:
            tempdirectory = pathlib.Path(tempdirectory)
            for i, page in enumerate(pages, start=1):
                file_name = '{}.jpg'.format(i)
                image_path = tempdirectory.joinpath(file_name)
                page.save(str(image_path))
                sleep(0.2)
                model = RulePageModel.objects.create(book=self, sortid=i)
                model.image.save(file_name, File(open(image_path, 'rb')))
                model.save()

    class Meta:
        verbose_name = _('Rule Book')
        verbose_name_plural = _('Rule Book')
        ordering = ['sortid', ]

    def __str__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rule_book_model.py ends here
