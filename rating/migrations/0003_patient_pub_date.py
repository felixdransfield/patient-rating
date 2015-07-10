# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20150608_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pub_date',
            field=models.DateTimeField(default='2015-08-06 13:46', verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
