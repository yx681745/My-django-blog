# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-05 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180305_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]