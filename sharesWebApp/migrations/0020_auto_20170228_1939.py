# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0019_auto_20170221_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Summary',
                'verbose_name': 'Resumen',
                'verbose_name_plural': 'Resumenes',
            },
        ),
        migrations.AlterField(
            model_name='share',
            name='change',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, verbose_name='Cambio (%)'),
        ),
    ]