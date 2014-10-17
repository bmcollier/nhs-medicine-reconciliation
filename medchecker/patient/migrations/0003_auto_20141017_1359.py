# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20141017_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='hospital_id',
            field=models.CharField(default=b'14135507783', unique=True, max_length=100, editable=False),
        ),
    ]
