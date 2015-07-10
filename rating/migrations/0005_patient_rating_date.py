# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_remove_patient_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='rating_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 8, 12, 48, 39, 470583, tzinfo=utc), verbose_name=b'date of rating'),
            preserve_default=False,
        ),
    ]
