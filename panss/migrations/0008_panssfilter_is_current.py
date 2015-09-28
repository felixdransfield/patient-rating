# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0007_auto_20150921_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='panssfilter',
            name='is_current',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
