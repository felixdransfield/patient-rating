# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0007_patient_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='PANSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date of rating', blank=True)),
                ('Q1', models.IntegerField()),
                ('Q2', models.IntegerField()),
                ('Q3', models.IntegerField()),
                ('Q4', models.IntegerField()),
                ('Q5', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rating_1',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rating_2',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rating_date',
        ),
        migrations.AddField(
            model_name='patient',
            name='DOA',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date of admission', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='DOB',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date of birth', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='DOD',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date of discharge', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital_id',
            field=models.IntegerField(default=1234567890, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)]),
            preserve_default=False,
        ),

    ]
