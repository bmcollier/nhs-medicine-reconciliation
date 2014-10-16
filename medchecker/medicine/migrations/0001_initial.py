# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActualMedicinalProduct',
            fields=[
                ('apid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True, blank=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True, blank=True)),
                ('desc', models.CharField(max_length=255)),
                ('nmdt', models.DateField(null=True, blank=True)),
                ('nm_prev', models.CharField(max_length=255, null=True, blank=True)),
                ('suppcd', models.IntegerField()),
                ('lic_authcd', models.IntegerField()),
                ('lic_auth_prevcd', models.IntegerField(null=True, blank=True)),
                ('lic_authchangecd', models.IntegerField(null=True, blank=True)),
                ('lic_authchangedt', models.DateField(null=True, blank=True)),
                ('combprodcd', models.IntegerField(null=True, blank=True)),
                ('flavourcd', models.IntegerField(null=True, blank=True)),
                ('ema', models.IntegerField(null=True, blank=True)),
                ('parallel_import', models.IntegerField(null=True, blank=True)),
                ('avail_restrictcd', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Actual Medicinal Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActualMedicinalProductPack',
            fields=[
                ('appid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True, blank=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True, blank=True)),
                ('combpackcd', models.IntegerField(null=True, blank=True)),
                ('legal_catcd', models.IntegerField()),
                ('subp', models.CharField(max_length=255, null=True, blank=True)),
                ('disccd', models.IntegerField(null=True, blank=True)),
                ('discdt', models.DateField(null=True, blank=True)),
                ('gtin', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(regex=b'|([0-9]{13})|([0-9]{14})', message=b'GTIN must be 13 or 14 digits.')])),
                ('gtin_startdt', models.DateField(null=True, blank=True)),
                ('gtin_enddt', models.DateField(null=True, blank=True)),
                ('apid', models.ForeignKey(to='medicine.ActualMedicinalProduct', db_column=b'apid')),
            ],
            options={
                'verbose_name': 'Actual Medicinal Product Pack',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VirtualMedicinalProduct',
            fields=[
                ('vpid', models.IntegerField(serialize=False, primary_key=True)),
                ('vpiddt', models.DateField(null=True, blank=True)),
                ('vpidprev', models.IntegerField(null=True, blank=True)),
                ('invalid', models.IntegerField(null=True, blank=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True, blank=True)),
                ('basiscd', models.IntegerField()),
                ('nmdt', models.DateField(null=True, blank=True)),
                ('nmprev', models.CharField(max_length=255, null=True, blank=True)),
                ('basis_prevcd', models.IntegerField(null=True, blank=True)),
                ('nmchangecd', models.IntegerField(null=True, blank=True)),
                ('combprodcd', models.IntegerField(null=True, blank=True)),
                ('pres_statcd', models.IntegerField()),
                ('sug_f', models.IntegerField(null=True, blank=True)),
                ('glu_f', models.IntegerField(null=True, blank=True)),
                ('pres_f', models.IntegerField(null=True, blank=True)),
                ('cfc_f', models.IntegerField(null=True, blank=True)),
                ('non_availcd', models.IntegerField(null=True, blank=True)),
                ('non_availdt', models.DateField(null=True, blank=True)),
                ('df_indcd', models.IntegerField(null=True, blank=True)),
                ('udfs', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
                ('udfs_uomcd', models.IntegerField(null=True, blank=True)),
                ('unit_dose_uomcd', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Virtual Medicinal Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VirtualMedicinalProductPack',
            fields=[
                ('vppid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True, blank=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True, blank=True)),
                ('qtyval', models.DecimalField(max_digits=7, decimal_places=2)),
                ('qty_uomcd', models.IntegerField()),
                ('combpackcd', models.IntegerField(null=True, blank=True)),
                ('vpid', models.ForeignKey(to='medicine.VirtualMedicinalProduct', db_column=b'vpid')),
            ],
            options={
                'verbose_name': 'Virtual Medicinal Product Pack',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VirtualTherapeuticMoiety',
            fields=[
                ('vtmid', models.IntegerField(serialize=False, primary_key=True)),
                ('invalid', models.IntegerField(null=True, blank=True)),
                ('nm', models.CharField(max_length=255)),
                ('abbrevnm', models.CharField(max_length=255, null=True, blank=True)),
                ('vtmidprev', models.CharField(max_length=255, null=True, blank=True)),
                ('vtmiddt', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Virtual Therapeutic Moiety',
                'verbose_name_plural': 'Virtual Therapeutic Moieties',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='virtualmedicinalproduct',
            name='vtmid',
            field=models.ForeignKey(db_column=b'vtmid', blank=True, to='medicine.VirtualTherapeuticMoiety', null=True),
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
