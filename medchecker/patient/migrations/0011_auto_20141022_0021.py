# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20141017_1359'),
        ('patient', '0010_patientmedication_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPMedication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('form', models.CharField(max_length=255)),
                ('strength', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('dose', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('special_instructions', models.TextField(null=True, blank=True)),
                ('reason', models.CharField(max_length=1000, null=True, blank=True)),
                ('comments', models.TextField(null=True, blank=True)),
                ('status', models.CharField(max_length=20, choices=[(b'UNVERIFIED', b'Unverified'), (b'VERIFIED', b'Verified'), (b'DELETED', b'Deleted')])),
                ('patient', models.ForeignKey(blank=True, to='patient.Patient', null=True)),
                ('virtual_medicinal_product', models.ForeignKey(to='medicine.VirtualMedicinalProduct', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patientmedication',
            name='route',
            field=models.CharField(default='oral', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientmedication',
            name='status',
            field=models.CharField(max_length=20, choices=[(b'UNVERIFIED', b'Unverified'), (b'VERIFIED', b'Verified'), (b'DELETED', b'Deleted')]),
        ),
    ]
