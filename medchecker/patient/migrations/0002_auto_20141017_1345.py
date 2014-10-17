# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='hospital_id',
            field=models.CharField(default=b'14135499286', unique=True, max_length=100, editable=False),
        ),
    ]
