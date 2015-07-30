# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0018_auto_20150717_0958'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=1, choices=[(b'1', b'Medication change'), (b'2', b'Management plan change'), (b'3', b'Other Stressor')])),
                ('DOE', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date of Event', blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(to='rating.Patient')),
            ],
        ),
    ]
