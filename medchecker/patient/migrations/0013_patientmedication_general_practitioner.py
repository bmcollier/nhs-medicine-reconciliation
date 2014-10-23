# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_auto_20141023_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedication',
            name='general_practitioner',
            field=models.ForeignKey(default=patient.models.get_random_gp, to='patient.GeneralPractitioner'),
            preserve_default=True,
        ),
    ]
