# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-14 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_auto_20180214_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantproposal',
            name='authors',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Members'),
        ),
    ]