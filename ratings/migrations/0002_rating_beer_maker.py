# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='beer_maker',
            field=models.TextField(blank=True),
        ),
    ]
