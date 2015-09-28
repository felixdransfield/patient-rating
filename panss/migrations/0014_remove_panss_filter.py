# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0013_remove_panss_p1_shown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panss',
            name='filter',
        ),
    ]
