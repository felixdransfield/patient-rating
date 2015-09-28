# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0010_auto_20150922_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='panss',
            name='filter',
            field=models.ForeignKey(default=16, to='panss.PANSSFilter'),
            preserve_default=False,
        ),
    ]
