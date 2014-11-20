# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0021_auto_20141118_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='source',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'RELATIVE', b'Relative of Patient'), (b'CARER', b'Carer of Patient'), (b'PATIENT', b'Patient'), (b'MEDICINE_BAG', b'Medicine Bag')]),
        ),
        migrations.AlterField(
            model_name='medication',
            name='status',
            field=models.CharField(default=b'0 UNVERIFIED', max_length=20, null=True, blank=True, choices=[(b'0 UNVERIFIED', b'Unverified'), (b'1 TAKING', b'Taking as prescribed'), (b'1 NOT AS PRESCRIBED', b'Taking, but not as prescribed'), (b'1 NOT TAKING', b'Not Taking'), (b'2 DELETED', b'Deleted')]),
        ),
        migrations.AlterField(
            model_name='medication',
            name='virtual_medicinal_product',
            field=models.ForeignKey(to='medicine.VirtualMedicinalProduct'),
        ),
    ]
