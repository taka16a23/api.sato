#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity_model_admin --

"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from publish.models.news_model import NewsModel
from publish.models.news_category_model import NewsCategoryModel

class ActivityModelAdmin(SummernoteModelAdmin):
    """ActivityModelAdmin

    ActivityModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    summernote_fields = (
        'body',
    )
    list_display = (
        'title',
        'status',
        'publish_date',
        'expiry_date',
    )
    list_editable = (
        'status',
    )
    ordering = (
        '-publish_date',
    )
    radio_fields = {
        'status': admin.HORIZONTAL,
    }

    def save_model(self, request, obj, form, change):
        super(ActivityModelAdmin, self).save_model(request, obj, form, change)
        if change:
            return
        newstitle = form.cleaned_data['title']
        news_category_model = NewsCategoryModel.objects.get(name=u'お知らせ')
        news = NewsModel.objects.create(
            title=newstitle,
            url=obj.get_absolute_url(),
            category=news_category_model,
            publish_date=obj.publish_date,
            expiry_date=obj.expiry_date,
            status=obj.status)
        obj.news = news
        obj.save()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity_model_admin.py ends here
