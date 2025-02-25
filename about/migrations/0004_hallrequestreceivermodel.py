# Generated by Django 5.0.4 on 2024-05-15 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_hallrequesthistorymodel_is_finished'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HallRequestReceiverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='name')),
                ('email', models.EmailField(help_text='example@example.com', max_length=254, verbose_name='email')),
                ('active', models.BooleanField(default=False, verbose_name='receive')),
                ('created_by', models.ForeignKey(db_column='created_by', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created_by')),
                ('modified_by', models.ForeignKey(db_column='modified_by', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified_by')),
            ],
            options={
                'verbose_name': 'Hall Request Reciever',
                'verbose_name_plural': 'Hall Request Reciever',
                'ordering': ['name'],
            },
        ),
    ]
