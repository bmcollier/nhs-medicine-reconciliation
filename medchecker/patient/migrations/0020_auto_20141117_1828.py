# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0019_medication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='daily_dose',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='daily_dose_units',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='frequency',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
