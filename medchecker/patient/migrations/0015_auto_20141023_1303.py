# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_auto_20141023_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='nhs_number',
            field=models.CharField(default=patient.models.generate_nhs_number, max_length=12, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{3} [0-9]{3} [0-9]{4}', message=b'NHS Number must be in the format 000 000 0000')]),
        ),
    ]
