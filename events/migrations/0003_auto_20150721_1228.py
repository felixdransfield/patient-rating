# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150721_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='DOE',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Date of Event', blank=True),
        ),
    ]
