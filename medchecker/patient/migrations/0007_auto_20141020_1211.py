# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20141017_1359'),
        ('patient', '0006_auto_20141020_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientmedication',
            name='virtual_medicinal_product_pack',
        ),
        migrations.AddField(
            model_name='patientmedication',
            name='virtual_medicinal_product',
            field=models.ForeignKey(default=None, to='medicine.VirtualMedicinalProduct'),
            preserve_default=False,
        ),
    ]
