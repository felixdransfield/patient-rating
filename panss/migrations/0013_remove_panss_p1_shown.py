# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panss', '0012_panss_p1_shown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panss',
            name='P1_shown',
        ),
    ]
