# Generated by Django 5.0.4 on 2024-05-25 20:10

import base.forms.validators.validate_pdf
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0005_alter_newsmodel_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
                ('status', models.CharField(choices=[('1', 'draft'), ('2', 'publish')], default='1', help_text='下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。', max_length=1, verbose_name='status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text='公開を選択すると、ここで設定した日時までは公開されません', null=True, verbose_name='publish date')),
                ('expiry_date', models.DateTimeField(blank=True, help_text='公開を選択すると、ここで設定した日時以降は公開されません', null=True, verbose_name='expiry date')),
                ('title', models.CharField(default='', max_length=255, verbose_name='title')),
                ('file', models.FileField(upload_to='boards/', validators=[base.forms.validators.validate_pdf.validate_pdf], verbose_name='PDF')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='board_thumbnails/', verbose_name='thumbnail')),
                ('created_by', models.ForeignKey(db_column='created_by', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created_by')),
                ('modified_by', models.ForeignKey(db_column='modified_by', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified_by')),
                ('news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publish.newsmodel')),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Board',
            },
        ),
    ]
