# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActualMedicinalProduct',
            fields=[
                ('apid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True)),
                ('desc', models.CharField(max_length=255)),
                ('nmdt', models.DateField(null=True)),
                ('nm_prev', models.CharField(max_length=255, null=True)),
                ('suppcd', models.IntegerField()),
                ('lic_authcd', models.IntegerField()),
                ('lic_auth_prevcd', models.IntegerField(null=True)),
                ('lic_authchangecd', models.IntegerField(null=True)),
                ('lic_authchangedt', models.DateField(null=True)),
                ('combprodcd', models.IntegerField(null=True)),
                ('flavourcd', models.IntegerField(null=True)),
                ('ema', models.IntegerField(null=True)),
                ('parallel_import', models.IntegerField(null=True)),
                ('avail_restrictcd', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActualMedicinalProductPack',
            fields=[
                ('appid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True)),
                ('combpackcd', models.IntegerField()),
                ('legal_catcd', models.IntegerField()),
                ('subp', models.CharField(max_length=255, null=True)),
                ('disccd', models.IntegerField()),
                ('discdt', models.DateField(null=True)),
                ('apid', models.ForeignKey(to='medicine.ActualMedicinalProduct', db_column=b'apid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VirtualMedicinalProduct',
            fields=[
                ('vpid', models.IntegerField(serialize=False, primary_key=True)),
                ('vpiddt', models.DateField(null=True)),
                ('vpidprev', models.IntegerField(null=True)),
                ('invalid', models.IntegerField(null=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True)),
                ('basiscd', models.IntegerField()),
                ('nmdt', models.DateField(null=True)),
                ('nmprev', models.CharField(max_length=255, null=True)),
                ('basis_prevcd', models.IntegerField(null=True)),
                ('nmchangecd', models.IntegerField(null=True)),
                ('combprodcd', models.IntegerField(null=True)),
                ('pres_statcd', models.IntegerField()),
                ('sug_f', models.IntegerField(null=True)),
                ('glu_f', models.IntegerField(null=True)),
                ('pres_f', models.IntegerField(null=True)),
                ('cfc_f', models.IntegerField(null=True)),
                ('non_availcd', models.IntegerField(null=True)),
                ('non_availdt', models.DateField(null=True)),
                ('df_indcd', models.IntegerField(null=True)),
                ('udfs', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('udfs_uomcd', models.IntegerField(null=True)),
                ('unit_dose_uomcd', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VirtualMedicinalProductPack',
            fields=[
                ('vppid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True)),
                ('qtyval', models.DecimalField(max_digits=7, decimal_places=2)),
                ('qty_uomcd', models.IntegerField()),
                ('combpackcd', models.IntegerField(null=True)),
                ('vpid', models.ForeignKey(to='medicine.VirtualMedicinalProduct', db_column=b'vpid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VirtualTherapeuticMoiety',
            fields=[
                ('vtmid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True)),
                ('vtmidprev', models.CharField(max_length=255, null=True)),
                ('vtmiddt', models.DateField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='virtualmedicinalproduct',
            name='vtmid',
            field=models.ForeignKey(to='medicine.VirtualTherapeuticMoiety', db_column=b'vtmid'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actualmedicinalproductpack',
            name='vppid',
            field=models.ForeignKey(to='medicine.VirtualMedicinalProductPack', db_column=b'vppid'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actualmedicinalproduct',
            name='vpid',
            field=models.ForeignKey(to='medicine.VirtualMedicinalProduct', db_column=b'vpid'),
            preserve_default=True,
        ),
    ]
