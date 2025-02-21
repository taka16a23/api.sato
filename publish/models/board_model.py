#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board_model --

"""
from time import sleep
import pathlib
import tempfile

from django.core.files import File
from django.db import models
from django.utils.translation import gettext_lazy as _
from pdf2image import convert_from_path

from base.forms.validators.validate_pdf import validate_pdf
from base.models.displayable_mixin import DisplayableMixin
from publish.models.news_category_model import NewsCategoryModel
from publish.models.news_model import NewsModel


class BoardModel(DisplayableMixin):
    """BoardModel

    BoardModel is a DisplayableMixin.
    Responsibility:
    """
    title = models.CharField(
        _('title'),
        max_length=255,
        blank=False,
        default='',
        null=False,
    )
    file = models.FileField(
        _('PDF'),
        upload_to='boards/',
        validators=[validate_pdf],
        null=False,
        blank=False,
    )
    thumbnail = models.ImageField(
        _('thumbnail'),
        upload_to='board_thumbnails/',
        blank=True,
        null=True,
    )
    news = models.ForeignKey(
        NewsModel,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text=_('create news if blank when first time')
    )

    def _save_thumnail(self, *args, **kwargs):
        pages = convert_from_path(self.file.path)
        if len(pages) <= 0:
            return
        file_name = 'tmp.jpg'
        with tempfile.TemporaryDirectory() as tempdirectory:
            tempdirectory = pathlib.Path(tempdirectory)
            image_path = tempdirectory.joinpath(file_name)
            pages[0].save(str(image_path))
            sleep(0.2)
            self.thumbnail.save(file_name, File(open(image_path, 'rb')), save=False)

    def _save_news(self, ):
        news_category = NewsCategoryModel.objects.filter(name='回覧').first()
        news_model = NewsModel.objects.create(
            title=self.title, category=news_category, url=self.file.url,
            status=self.status, publish_date=self.publish_date)
        news_model.save()
        self.news = news_model

    def save(self, *args, **kwargs):
        is_adding = self._state.adding
        super(BoardModel, self).save(*args, **kwargs)
        self._save_thumnail(*args, **kwargs)
        if is_adding != True:
            super(BoardModel, self).save(*args, **kwargs)
            return
        self._save_news()
        super(BoardModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Board')
        verbose_name_plural = _('Board')

    def __str__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# board_model.py ends here
