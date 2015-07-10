# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_patient_rating_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_1', models.IntegerField()),
                ('rating_2', models.IntegerField()),
                ('rating_date', models.DateTimeField(verbose_name=b'date of rating')),
                ('patient', models.ForeignKey(to='rating.Patient')),
            ],
        ),
    ]
