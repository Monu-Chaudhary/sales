# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='cid',
            field=models.IntegerField(default=0),
        ),
    ]
