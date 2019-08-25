# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20180210_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(error_messages={'blank': 'City can not be empty.', 'max_length': 'City must be less than 30 characters.'}, max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='location',
            name='number',
            field=models.CharField(error_messages={'blank': 'Number can not be empty.', 'max_length': 'Number must be less than 30 characters.'}, max_length=30, null=True, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='location',
            name='room',
            field=models.CharField(error_messages={'blank': 'Room can not be empty.', 'max_length': 'Room must be less than 30 characters.'}, max_length=30, null=True, verbose_name='Room'),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(error_messages={'blank': 'Street can not be empty.', 'max_length': 'Street must be less than 30 characters.'}, max_length=30, null=True, verbose_name='Street'),
        ),
    ]