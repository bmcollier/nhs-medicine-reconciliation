# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20141017_1359'),
        ('patient', '0018_auto_20141024_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('free_text', models.CharField(max_length=1000, null=True, blank=True)),
                ('form', models.CharField(max_length=255, null=True, blank=True)),
                ('strength', models.CharField(max_length=255, null=True, blank=True)),
                ('route', models.CharField(max_length=255)),
                ('dose', models.CharField(max_length=255, null=True, blank=True)),
                ('frequency', models.CharField(blank=True, max_length=255, null=True, choices=[(b'OD', b'Once daily'), (b'BD', b'Twice daily'), (b'TD', b'Three times daily'), (b'QD', b'Four times daily'), (b'HD', b'Five times daily'), (b'PD', b'Six times daily')])),
                ('duration', models.CharField(max_length=255, null=True, blank=True)),
                ('special_instructions', models.TextField(null=True, blank=True)),
                ('source', models.CharField(max_length=20, choices=[(b'RELATIVE', b'Relative of Patient'), (b'CARER', b'Carer of Patient'), (b'PATIENT', b'Patient'), (b'MEDICINE_BAG', b'Medicine Bag')])),
                ('reason', models.CharField(max_length=1000, null=True, blank=True)),
                ('status', models.CharField(default=b'0 UNVERIFIED', max_length=20, choices=[(b'0 UNVERIFIED', b'Unverified'), (b'1 TAKING', b'Taking as prescribed'), (b'1 NOT AS PRESCRIBED', b'Taking, but not as prescribed'), (b'1 NOT TAKING', b'Not Taking'), (b'2 DELETED', b'Deleted')])),
                ('last_taken', models.CharField(max_length=1000, null=True, blank=True)),
                ('barcode', models.CharField(max_length=20, null=True, blank=True)),
                ('vmp_derivation', models.CharField(max_length=255, null=True, blank=True)),
                ('dose_without_units', models.CharField(max_length=255, null=True, blank=True)),
                ('dose_units', models.CharField(blank=True, max_length=2, null=True, choices=[(b'g', b'grams'), (b'mg', b'milligrams')])),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('daily_dose', models.IntegerField(null=True, blank=True)),
                ('daily_dose_units', models.CharField(max_length=20, choices=[(b'g', b'grams'), (b'mg', b'milligrams')])),
                ('frequency_narrative', models.CharField(max_length=255, null=True, blank=True)),
                ('duration_start_date', models.DateTimeField(null=True, blank=True)),
                ('classification_type', models.CharField(max_length=20, choices=[(b'EHR', b'Electronic Health Record'), (b'GP', b'General Practitioner'), (b'OTHER', b'Other Source'), (b'HISTORY', b'Medication History'), (b'STOP', b'Stopped'), (b'SUSPEND', b'Suspended'), (b'CONTINUE', b'Continued')])),
                ('comments', models.TextField(null=True, blank=True)),
                ('patient', models.ForeignKey(blank=True, to='patient.Patient', null=True)),
                ('virtual_medicinal_product', models.ForeignKey(to='medicine.VirtualMedicinalProduct', null=True)),
                ('virtual_therapeutic_moiety', models.ForeignKey(to='medicine.VirtualTherapeuticMoiety', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
