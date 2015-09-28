# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0019_auto_20150805_1438'),
        ('panss', '0006_auto_20150921_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='panssfilter',
            name='patient',
            field=models.ForeignKey(default=1, to='rating.Patient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G1',
            field=models.BooleanField(verbose_name=b'Somatic Concerns'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G10',
            field=models.BooleanField(verbose_name=b'Disorientation'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G11',
            field=models.BooleanField(verbose_name=b'Poor Attention'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G12',
            field=models.BooleanField(verbose_name=b'Lack of Judgement and Insight'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G13',
            field=models.BooleanField(verbose_name=b'Disturbance of Volition'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G14',
            field=models.BooleanField(verbose_name=b'Poor Impulse Control'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G15',
            field=models.BooleanField(verbose_name=b'Preoccupation'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G16',
            field=models.BooleanField(verbose_name=b'Active Social Avoidance'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G2',
            field=models.BooleanField(verbose_name=b'Anxiety'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G3',
            field=models.BooleanField(verbose_name=b'Guilt Feelings'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G4',
            field=models.BooleanField(verbose_name=b'Tension'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G5',
            field=models.BooleanField(verbose_name=b'Mannerisms and Posturing'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G6',
            field=models.BooleanField(verbose_name=b'Depression'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G7',
            field=models.BooleanField(verbose_name=b'Motor Retardation'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G8',
            field=models.BooleanField(verbose_name=b'Uncooperativeness'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='G9',
            field=models.BooleanField(verbose_name=b'Unusual Though Content'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N1',
            field=models.BooleanField(verbose_name=b'Blunted Affect'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N2',
            field=models.BooleanField(verbose_name=b'Emotional Withdrawal'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N3',
            field=models.BooleanField(verbose_name=b'Poor Rapport'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N4',
            field=models.BooleanField(verbose_name=b'Passive/Apathetic Social Withdrawal'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N5',
            field=models.BooleanField(verbose_name=b'Difficulty in Abstract Thinking'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N6',
            field=models.BooleanField(verbose_name=b'Lack of Spontaneity'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='N7',
            field=models.BooleanField(verbose_name=b'Stereotyped Thinking'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P1',
            field=models.BooleanField(verbose_name=b'Delusions'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P2',
            field=models.BooleanField(verbose_name=b'Conceptual Disorganisation'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P3',
            field=models.BooleanField(verbose_name=b'Hallucinatory Behaviour'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P4',
            field=models.BooleanField(verbose_name=b'Excitement'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P5',
            field=models.BooleanField(verbose_name=b'Grandiosity'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P6',
            field=models.BooleanField(verbose_name=b'Suspiciousness/Persecution'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='P7',
            field=models.BooleanField(verbose_name=b'Hostility'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='S1',
            field=models.BooleanField(verbose_name=b'Anger'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='S2',
            field=models.BooleanField(verbose_name=b'Difficulty in Delaying Gratification'),
        ),
        migrations.AlterField(
            model_name='panssfilter',
            name='S3',
            field=models.BooleanField(verbose_name=b'Affective Lability'),
        ),
    ]
