# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient_id', models.CharField(max_length=10)),
                ('rating_1', models.IntegerField()),
                ('rating_2', models.IntegerField()),
            ],
        ),
    ]
