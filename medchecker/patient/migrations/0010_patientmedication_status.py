# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20141020_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedication',
            name='status',
            field=models.CharField(default='UNVERIFIED', max_length=20, choices=[(b'UNVERIFIED', b'Unverified'), (b'VERIFIED', b'Verified')]),
            preserve_default=False,
        ),
    ]
