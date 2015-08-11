# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0002_fullpanss'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullpanss',
            name='is_admission',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fullpanss',
            name='is_current',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fullpanss',
            name='is_discharge',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
