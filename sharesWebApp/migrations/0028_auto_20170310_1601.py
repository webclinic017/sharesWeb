# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0027_auto_20170308_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['dateSell', 'dateBuy'], 'verbose_name': 'Transacci\xf3n', 'verbose_name_plural': 'Transacciones'},
        ),
        migrations.AlterField(
            model_name='sharehistory',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=12, null=True, verbose_name='Volumen'),
        ),
    ]