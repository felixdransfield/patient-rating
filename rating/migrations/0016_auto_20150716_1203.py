# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0015_auto_20150713_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='DOA',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date of admission', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DOB',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date of birth', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DOD',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date of discharge', blank=True),
        ),
    ]
