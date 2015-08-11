# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0018_auto_20150717_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panss',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='panss',
            name='patient',
        ),
        migrations.DeleteModel(
            name='PANSS',
        ),
    ]
