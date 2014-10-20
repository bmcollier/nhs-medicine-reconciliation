# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20141020_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedication',
            name='patient',
            field=models.ForeignKey(blank=True, to='patient.Patient', null=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='virtual_medicinal_product',
            field=models.ForeignKey(to='medicine.VirtualMedicinalProduct', null=True),
        ),
    ]
