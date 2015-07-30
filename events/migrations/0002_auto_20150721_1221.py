# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
