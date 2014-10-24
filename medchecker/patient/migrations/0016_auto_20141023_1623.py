# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0015_auto_20141023_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedication',
            name='free_text',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gpmedication',
            name='dose',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gpmedication',
            name='duration',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gpmedication',
            name='form',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gpmedication',
            name='strength',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='dose',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='duration',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='form',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='status',
            field=models.CharField(default=b'UNVERIFIED', max_length=20, choices=[(b'UNVERIFIED', b'Unverified'), (b'VERIFIED', b'Verified'), (b'DELETED', b'Deleted')]),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='strength',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
