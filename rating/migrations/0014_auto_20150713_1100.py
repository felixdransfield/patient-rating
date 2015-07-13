# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0013_auto_20150710_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='HCR20',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date of rating', blank=True)),
                ('H1', models.IntegerField(verbose_name=b'Previous Violence')),
                ('H2', models.IntegerField(verbose_name=b'Young Age at First Violent Incident')),
                ('H3', models.IntegerField(verbose_name=b'Relationship Instability')),
                ('H4', models.IntegerField(verbose_name=b'Employment Problems')),
                ('H5', models.IntegerField(verbose_name=b'Substance Use Problems')),
                ('H6', models.IntegerField(verbose_name=b'Major Mental Illness')),
                ('H7', models.IntegerField(verbose_name=b'Psychopathy')),
                ('H8', models.IntegerField(verbose_name=b'Early Maladjustment')),
                ('H9', models.IntegerField(verbose_name=b'Personality Disorder')),
                ('H10', models.IntegerField(verbose_name=b'Prior Supervision Failure')),
                ('C1', models.IntegerField(verbose_name=b'Lack of Insight')),
                ('C2', models.IntegerField(verbose_name=b'Negative Attitudes')),
                ('C3', models.IntegerField(verbose_name=b'Active Symptoms of Major Mental Illness')),
                ('C4', models.IntegerField(verbose_name=b'Impulsivity')),
                ('C5', models.IntegerField(verbose_name=b'Unresponsive to Treatment')),
                ('R1', models.IntegerField(verbose_name=b'Plans Lack Feasibility')),
                ('R2', models.IntegerField(verbose_name=b'Exposure to Destabilizers')),
                ('R3', models.IntegerField(verbose_name=b'Lack of Personal Support')),
                ('R4', models.IntegerField(verbose_name=b'Noncompliance with Remediation Attempts')),
                ('R5', models.IntegerField(verbose_name=b'Stress')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(to='rating.Patient')),
            ],
        ),
        migrations.AlterField(
            model_name='panss',
            name='G1',
            field=models.IntegerField(verbose_name=b'Somatic Concerns'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G10',
            field=models.IntegerField(verbose_name=b'Disorientation'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G11',
            field=models.IntegerField(verbose_name=b'Poor Attention'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G12',
            field=models.IntegerField(verbose_name=b'Lack of Judgement and Insight'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G13',
            field=models.IntegerField(verbose_name=b'Disturbance of Volition'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G14',
            field=models.IntegerField(verbose_name=b'Poor Impulse Control'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G15',
            field=models.IntegerField(verbose_name=b'Preoccupation'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G16',
            field=models.IntegerField(verbose_name=b'Active Social Avoidance'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G2',
            field=models.IntegerField(verbose_name=b'Anxiety'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G3',
            field=models.IntegerField(verbose_name=b'Guilt Feelings'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G4',
            field=models.IntegerField(verbose_name=b'Tension'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G5',
            field=models.IntegerField(verbose_name=b'Mannerisms and Posturing'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G6',
            field=models.IntegerField(verbose_name=b'Depression'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G7',
            field=models.IntegerField(verbose_name=b'Motor Retardation'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G8',
            field=models.IntegerField(verbose_name=b'Uncooperativeness'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G9',
            field=models.IntegerField(verbose_name=b'Unusual Though Content'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N1',
            field=models.IntegerField(verbose_name=b'Blunted Affect'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N2',
            field=models.IntegerField(verbose_name=b'Emotional Withdrawal'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N3',
            field=models.IntegerField(verbose_name=b'Poor Rapport'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N4',
            field=models.IntegerField(verbose_name=b'Passive/Apathetic Social Withdrawal'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N5',
            field=models.IntegerField(verbose_name=b'Difficulty in Abstract Thinking'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N6',
            field=models.IntegerField(verbose_name=b'Lack of Spontaneity'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N7',
            field=models.IntegerField(verbose_name=b'Stereotyped Thinking'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P1',
            field=models.IntegerField(verbose_name=b'Delusions'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P2',
            field=models.IntegerField(verbose_name=b'Conceptual Disorganisation'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P3',
            field=models.IntegerField(verbose_name=b'Hallucinatory Behaviour'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P4',
            field=models.IntegerField(verbose_name=b'Excitement'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P5',
            field=models.IntegerField(verbose_name=b'Grandiosity'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P6',
            field=models.IntegerField(verbose_name=b'Suspiciousness/Persecution'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P7',
            field=models.IntegerField(verbose_name=b'Hostility'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='S1',
            field=models.IntegerField(verbose_name=b'Anger'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='S2',
            field=models.IntegerField(verbose_name=b'Difficulty in Delaying Gratification'),
        ),
        migrations.AlterField(
            model_name='panss',
            name='S3',
            field=models.IntegerField(verbose_name=b'Affective Lability'),
        ),
    ]
