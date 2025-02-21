# Generated by Django 5.0.4 on 2024-05-11 18:29

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SatoFormatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
                ('status', models.CharField(choices=[('1', 'draft'), ('2', 'publish')], default='1', help_text='下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。', max_length=1, verbose_name='status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text='公開を選択すると、ここで設定した日時までは公開されません', null=True, verbose_name='publish date')),
                ('expiry_date', models.DateTimeField(blank=True, help_text='公開を選択すると、ここで設定した日時以降は公開されません', null=True, verbose_name='expiry date')),
                ('title', models.CharField(max_length=255, verbose_name='format name')),
                ('description', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='description')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='formats', verbose_name='PDF')),
                ('form', models.URLField(blank=True, default=None, null=True, verbose_name='form address')),
                ('sortid', models.IntegerField(db_index=True, default=0, help_text='サイトで昇順に並びます', verbose_name=' ')),
                ('created_by', models.ForeignKey(db_column='created_by', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created_by')),
                ('modified_by', models.ForeignKey(db_column='modified_by', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified_by')),
            ],
            options={
                'verbose_name': 'Sato Formats',
                'verbose_name_plural': 'Sato Formats',
                'ordering': ['sortid'],
            },
        ),
    ]
