# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20141017_1359'),
        ('patient', '0003_auto_20141017_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('form', models.CharField(max_length=255)),
                ('strength', models.CharField(max_length=255)),
                ('dose', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=512)),
                ('special_instructions', models.TextField()),
                ('comments', models.TextField()),
                ('patient', models.ForeignKey(to='patient.Patient')),
                ('virtual_medicinal_product_pack', models.ForeignKey(to='medicine.VirtualMedicinalProductPack')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hospital_id',
            field=models.CharField(default=b'14135537429', unique=True, max_length=100, editable=False),
        ),
    ]
