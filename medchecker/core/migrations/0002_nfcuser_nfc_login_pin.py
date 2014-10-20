# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfcuser',
            name='nfc_login_pin',
            field=models.IntegerField(default=1111, max_length=4),
            preserve_default=False,
        ),
    ]
