# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0020_auto_20141117_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='classification_type',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'EHR', b'Electronic Health Record'), (b'GP', b'General Practitioner'), (b'OTHER', b'Other Source'), (b'HISTORY', b'Medication History'), (b'STOP', b'Stopped'), (b'SUSPEND', b'Suspended'), (b'CONTINUE', b'Continued')]),
        ),
        migrations.AlterField(
            model_name='medication',
            name='route',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='virtual_medicinal_product',
            field=models.ForeignKey(blank=True, to='medicine.VirtualMedicinalProduct', null=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='virtual_therapeutic_moiety',
            field=models.ForeignKey(blank=True, to='medicine.VirtualTherapeuticMoiety', null=True),
        ),
    ]
