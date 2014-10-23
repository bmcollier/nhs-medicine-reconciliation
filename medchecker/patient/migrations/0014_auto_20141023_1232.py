# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_patientmedication_general_practitioner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientmedication',
            name='general_practitioner',
        ),
        migrations.AddField(
            model_name='patient',
            name='general_practitioner',
            field=models.ForeignKey(default=patient.models.get_random_gp, to='patient.GeneralPractitioner'),
            preserve_default=True,
        ),
    ]
