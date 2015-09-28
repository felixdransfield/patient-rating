# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0005_auto_20150921_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panssfilter',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='panssfilter',
            name='patient',
        ),
    ]
