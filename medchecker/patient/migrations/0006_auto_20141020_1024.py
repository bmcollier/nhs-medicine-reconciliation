# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_auto_20141017_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='hospital_id',
            field=models.CharField(default=patient.models.generate_hospital_id, unique=True, max_length=100, editable=False),
        ),
    ]
