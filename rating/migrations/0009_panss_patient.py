# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0008_auto_20150623_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='panss',
            name='patient',
            field=models.ForeignKey(default=4, to='rating.Patient'),
            preserve_default=False,
        ),
    ]
