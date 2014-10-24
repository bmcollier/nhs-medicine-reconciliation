# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_auto_20141024_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedication',
            name='last_taken',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=patient.models.generate_dob),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(default=patient.models.generate_sex, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
