# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0022_auto_20141118_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='dose_units',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
