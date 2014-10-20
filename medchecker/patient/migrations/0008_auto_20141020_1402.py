# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_auto_20141020_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedication',
            name='comments',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='patient',
            field=models.ForeignKey(to='patient.Patient', blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='reason',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='special_instructions',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='virtual_medicinal_product',
            field=models.ForeignKey(to='medicine.VirtualMedicinalProduct', blank=True),
        ),
    ]
