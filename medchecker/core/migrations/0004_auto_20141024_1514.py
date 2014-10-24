# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141023_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfcuser',
            name='nfc_login_pin',
            field=models.IntegerField(default=1111, max_length=4),
        ),
        migrations.AlterField(
            model_name='nfcuser',
            name='nhs_trust',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='nfcuser',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
