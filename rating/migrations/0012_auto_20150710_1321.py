# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0011_auto_20150710_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panss',
            name='G1',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G10',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G11',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G12',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G13',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G14',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G15',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G16',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G2',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G3',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G4',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G5',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G6',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G7',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G8',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='G9',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N1',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N2',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N3',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N4',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N5',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N6',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='N7',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P1',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P2',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P3',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P4',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P5',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P6',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='P7',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='S1',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='S2',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
        migrations.AlterField(
            model_name='panss',
            name='S3',
            field=models.IntegerField(max_length=1, choices=[(b'1', b'Better'), (b'0', b'Same'), (b'-1', b'Worse')]),
        ),
    ]
