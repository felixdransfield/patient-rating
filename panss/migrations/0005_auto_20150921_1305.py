# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0019_auto_20150805_1438'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panss', '0004_auto_20150810_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='PANSSFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('P1', models.BooleanField()),
                ('P2', models.BooleanField()),
                ('P3', models.BooleanField()),
                ('P4', models.BooleanField()),
                ('P5', models.BooleanField()),
                ('P6', models.BooleanField()),
                ('P7', models.BooleanField()),
                ('N1', models.BooleanField()),
                ('N2', models.BooleanField()),
                ('N3', models.BooleanField()),
                ('N4', models.BooleanField()),
                ('N5', models.BooleanField()),
                ('N6', models.BooleanField()),
                ('N7', models.BooleanField()),
                ('G1', models.BooleanField()),
                ('G2', models.BooleanField()),
                ('G3', models.BooleanField()),
                ('G4', models.BooleanField()),
                ('G5', models.BooleanField()),
                ('G6', models.BooleanField()),
                ('G7', models.BooleanField()),
                ('G8', models.BooleanField()),
                ('G9', models.BooleanField()),
                ('G10', models.BooleanField()),
                ('G11', models.BooleanField()),
                ('G12', models.BooleanField()),
                ('G13', models.BooleanField()),
                ('G14', models.BooleanField()),
                ('G15', models.BooleanField()),
                ('G16', models.BooleanField()),
                ('S1', models.BooleanField()),
                ('S2', models.BooleanField()),
                ('S3', models.BooleanField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(to='rating.Patient')),
            ],
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G1',
            field=models.IntegerField(default=1, verbose_name=b'G1 - Somatic Concerns'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G10',
            field=models.IntegerField(default=1, verbose_name=b'G10 - Disorientation'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G11',
            field=models.IntegerField(default=1, verbose_name=b'G11 - Poor Attention'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G12',
            field=models.IntegerField(default=1, verbose_name=b'G12 - Lack of Judgement and Insight'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G13',
            field=models.IntegerField(default=1, verbose_name=b'G13 - Disturbance of Volition'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G14',
            field=models.IntegerField(default=1, verbose_name=b'G14 - Poor Impulse Control'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G15',
            field=models.IntegerField(default=1, verbose_name=b'G15 - Preoccupation'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G16',
            field=models.IntegerField(default=1, verbose_name=b'G16 - Active Social Avoidance'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G2',
            field=models.IntegerField(default=1, verbose_name=b'G2 - Anxiety'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G3',
            field=models.IntegerField(default=1, verbose_name=b'G3 - Guilt Feelings'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G4',
            field=models.IntegerField(default=1, verbose_name=b'G4 - Tension'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G5',
            field=models.IntegerField(default=1, verbose_name=b'G5 - Mannerisms and Posturing'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G6',
            field=models.IntegerField(default=1, verbose_name=b'G6 - Depression'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G7',
            field=models.IntegerField(default=1, verbose_name=b'G7 - Motor Retardation'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G8',
            field=models.IntegerField(default=1, verbose_name=b'G8 - Uncooperativeness'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='G9',
            field=models.IntegerField(default=1, verbose_name=b'G9 - Unusual Though Content'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N1',
            field=models.IntegerField(default=1, verbose_name=b'N1 - Blunted Affect'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N2',
            field=models.IntegerField(default=1, verbose_name=b'N2 - Emotional Withdrawal'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N3',
            field=models.IntegerField(default=1, verbose_name=b'N3 - Poor Rapport'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N4',
            field=models.IntegerField(default=1, verbose_name=b'N4 - Passive/Apathetic Social Withdrawal'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N5',
            field=models.IntegerField(default=1, verbose_name=b'N5 - Difficulty in Abstract Thinking'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N6',
            field=models.IntegerField(default=1, verbose_name=b'N6 - Lack of Spontaneity'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='N7',
            field=models.IntegerField(default=1, verbose_name=b'N7 - Stereotyped Thinking'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P1',
            field=models.IntegerField(default=1, verbose_name=b'P1 - Delusions'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P2',
            field=models.IntegerField(default=1, verbose_name=b'P2 - Conceptual Disorganisation'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P3',
            field=models.IntegerField(default=1, verbose_name=b'P3 - Hallucinatory Behaviour'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P4',
            field=models.IntegerField(default=1, verbose_name=b'P4 - Excitement'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P5',
            field=models.IntegerField(default=1, verbose_name=b'P5 - Grandiosity'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P6',
            field=models.IntegerField(default=1, verbose_name=b'P6 - Suspiciousness/Persecution'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='P7',
            field=models.IntegerField(default=1, verbose_name=b'P7 - Hostility'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='S1',
            field=models.IntegerField(default=1, verbose_name=b'S1 - Anger'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='S2',
            field=models.IntegerField(default=1, verbose_name=b'S2 - Difficulty in Delaying Gratification'),
        ),
        migrations.AlterField(
            model_name='fullpanss',
            name='S3',
            field=models.IntegerField(default=1, verbose_name=b'S3 - Affective Lability'),
        ),
    ]
