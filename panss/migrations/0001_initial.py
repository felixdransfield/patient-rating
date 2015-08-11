# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0019_auto_20150805_1438'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PANSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'date of rating', blank=True)),
                ('P1', models.IntegerField(default=0, verbose_name=b'P1 - Delusions')),
                ('P2', models.IntegerField(default=0, verbose_name=b'P2 - Conceptual Disorganisation')),
                ('P3', models.IntegerField(default=0, verbose_name=b'P3 - Hallucinatory Behaviour')),
                ('P4', models.IntegerField(default=0, verbose_name=b'P4 - Excitement')),
                ('P5', models.IntegerField(default=0, verbose_name=b'P5 - Grandiosity')),
                ('P6', models.IntegerField(default=0, verbose_name=b'P6 - Suspiciousness/Persecution')),
                ('P7', models.IntegerField(default=0, verbose_name=b'P7 - Hostility')),
                ('N1', models.IntegerField(default=0, verbose_name=b'N1 - Blunted Affect')),
                ('N2', models.IntegerField(default=0, verbose_name=b'N2 - Emotional Withdrawal')),
                ('N3', models.IntegerField(default=0, verbose_name=b'N3 - Poor Rapport')),
                ('N4', models.IntegerField(default=0, verbose_name=b'N4 - Passive/Apathetic Social Withdrawal')),
                ('N5', models.IntegerField(default=0, verbose_name=b'N5 - Difficulty in Abstract Thinking')),
                ('N6', models.IntegerField(default=0, verbose_name=b'N6 - Lack of Spontaneity')),
                ('N7', models.IntegerField(default=0, verbose_name=b'N7 - Stereotyped Thinking')),
                ('G1', models.IntegerField(default=0, verbose_name=b'G1 - Somatic Concerns')),
                ('G2', models.IntegerField(default=0, verbose_name=b'G2 - Anxiety')),
                ('G3', models.IntegerField(default=0, verbose_name=b'G3 - Guilt Feelings')),
                ('G4', models.IntegerField(default=0, verbose_name=b'G4 - Tension')),
                ('G5', models.IntegerField(default=0, verbose_name=b'G5 - Mannerisms and Posturing')),
                ('G6', models.IntegerField(default=0, verbose_name=b'G6 - Depression')),
                ('G7', models.IntegerField(default=0, verbose_name=b'G7 - Motor Retardation')),
                ('G8', models.IntegerField(default=0, verbose_name=b'G8 - Uncooperativeness')),
                ('G9', models.IntegerField(default=0, verbose_name=b'G9 - Unusual Though Content')),
                ('G10', models.IntegerField(default=0, verbose_name=b'G10 - Disorientation')),
                ('G11', models.IntegerField(default=0, verbose_name=b'G11 - Poor Attention')),
                ('G12', models.IntegerField(default=0, verbose_name=b'G12 - Lack of Judgement and Insight')),
                ('G13', models.IntegerField(default=0, verbose_name=b'G13 - Disturbance of Volition')),
                ('G14', models.IntegerField(default=0, verbose_name=b'G14 - Poor Impulse Control')),
                ('G15', models.IntegerField(default=0, verbose_name=b'G15 - Preoccupation')),
                ('G16', models.IntegerField(default=0, verbose_name=b'G16 - Active Social Avoidance')),
                ('S1', models.IntegerField(default=0, verbose_name=b'S1 - Anger')),
                ('S2', models.IntegerField(default=0, verbose_name=b'S2 - Difficulty in Delaying Gratification')),
                ('S3', models.IntegerField(default=0, verbose_name=b'S3 - Affective Lability')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(related_name='patientname', to='rating.Patient')),
            ],
        ),
    ]
