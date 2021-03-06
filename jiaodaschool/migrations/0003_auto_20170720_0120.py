# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiaodaschool', '0002_auto_20170720_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examine',
            name='average',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='examine',
            name='first_quartile',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='examine',
            name='highest_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='examine',
            name='lowest_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='examine',
            name='median',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='examine',
            name='third_quartile',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
