# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_patient_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='pub_date',
        ),
    ]
