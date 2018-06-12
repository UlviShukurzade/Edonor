# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-12 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_myuser_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='blood_group',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], default=1, null=True),
        ),
    ]
