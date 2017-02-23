# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0014_auto_20170219_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='euro',
        ),
        migrations.AddField(
            model_name='currency',
            name='lastValue',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Valor'),
        ),
    ]
