# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-14 20:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(error_messages={'blank': 'Username can not be empty.', 'max_length': 'Username must be less than 30 characters.', 'null': 'Username is a required field.', 'unique': 'This Username has already been registered.'}, max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^(?=.{3,30}$)(?![_.+-])(?!.*[_.+-]{2})[a-zA-Z0-9._+-]+(?<![_.+-])$', ' 1_Only contains alphanumeric chars and (+, -, _, .).  2_(+, -, _, .) can not be at the end or start of username. 3_(+, -, _, .) can not be next to each other. 4_(+, -, _, .) can not be used multiple times in a row. 5_Number of characters must be between 3 to 30.')]),
        ),
    ]
