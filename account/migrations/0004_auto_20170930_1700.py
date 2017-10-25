# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170930_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2010-01-01', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.DecimalField(decimal_places=2, default='10', max_digits=10),
        ),
    ]
