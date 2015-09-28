# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0011_panss_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='panss',
            name='P1_shown',
            field=models.BooleanField(default=1, verbose_name=b'Delusions'),
            preserve_default=False,
        ),
    ]
