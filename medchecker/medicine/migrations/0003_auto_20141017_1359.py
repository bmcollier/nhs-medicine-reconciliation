# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_auto_20141017_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualmedicinalproductpack',
            name='gtin',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(regex=b'|([0-9]{13})|([0-9]{14})', message=b'GTIN must be 13 or 14 digits.')]),
        ),
    ]
