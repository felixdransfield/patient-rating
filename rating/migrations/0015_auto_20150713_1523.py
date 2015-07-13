# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0014_auto_20150713_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hcr20',
            name='R5',
            field=models.IntegerField(verbose_name=b'Depression'),
        ),
    ]
