# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_logo', models.FileField(upload_to='')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.CharField(max_length=50)),
                ('item_status', models.CharField(max_length=40)),
                ('seller_info', models.CharField(max_length=1000)),
                ('general_detail', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('item_spec', models.CharField(max_length=500)),
                ('delivery', models.CharField(max_length=75)),
            ],
        ),
    ]
