# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20171009_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_status',
            field=models.CharField(choices=[('superuser', 'Суперпользовател'), ('partner', 'Партнёр'), ('bank', 'Кредитная организация'), ('user', 'Пользователь')], default='user', max_length=20, verbose_name='Группа пользователя'),
        ),
    ]