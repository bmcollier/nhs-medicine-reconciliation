# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0016_auto_20141023_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.AddField(
            model_name='patient',
            name='county',
            field=models.CharField(default=patient.models.generate_county, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='post_code',
            field=models.CharField(default=patient.models.generate_postcode, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='street',
            field=models.CharField(default=patient.models.generate_street, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='town',
            field=models.CharField(default=patient.models.generate_town, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default=patient.models.generate_first_name, max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default=patient.models.generate_last_name, max_length=255),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='status',
            field=models.CharField(default=b'0 UNVERIFIED', max_length=20, choices=[(b'0 UNVERIFIED', b'Unverified'), (b'1 TAKING', b'Taking as prescribed'), (b'1 NOT AS PRESCRIBED', b'Taking, but not as prescribed'), (b'1 NOT TAKING', b'Not Taking'), (b'2 DELETED', b'Deleted')]),
        ),
    ]
