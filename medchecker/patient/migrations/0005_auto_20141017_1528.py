# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20141017_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedication',
            name='reason',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientmedication',
            name='source',
            field=models.CharField(default='', max_length=20, choices=[(b'RELATIVE', b'Relative of Patient'), (b'CARER', b'Carer of Patient'), (b'PATIENT', b'Patient'), (b'MEDICINE_BAG', b'Medicine Bag')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='hospital_id',
            field=models.CharField(default=b'14135560868', unique=True, max_length=100, editable=False),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='duration',
            field=models.CharField(max_length=255),
        ),
    ]
