# Generated by Django 5.1.3 on 2025-01-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='halleventmodel',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halleventmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='halleventmodel',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halleventmodel',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
