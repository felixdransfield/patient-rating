# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0017_auto_20150716_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hcr20',
            name='rating_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date of rating', blank=True),
        ),
        migrations.AlterField(
            model_name='panss',
            name='patient',
            field=models.ForeignKey(related_name='patientname', to='rating.Patient'),
        ),
    ]
