# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141024_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfcuser',
            name='role',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
