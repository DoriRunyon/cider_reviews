# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 03:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_rating_beer_maker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='beer_maker',
            new_name='brewer_name',
        ),
    ]