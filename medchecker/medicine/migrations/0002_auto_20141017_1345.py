# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='apid',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='avail_restrictcd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='combprodcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='ema',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='flavourcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='invalid',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='lic_auth_prevcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='lic_authcd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='lic_authchangecd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='parallel_import',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproduct',
            name='suppcd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproductpack',
            name='appid',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproductpack',
            name='combpackcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproductpack',
            name='disccd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproductpack',
            name='invalid',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actualmedicinalproductpack',
            name='legal_catcd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='basis_prevcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='basiscd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='cfc_f',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='combprodcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='df_indcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='glu_f',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='invalid',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='nmchangecd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='non_availcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='pres_f',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='pres_statcd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='sug_f',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='udfs_uomcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='unit_dose_uomcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='vpid',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproduct',
            name='vpidprev',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproductpack',
            name='combpackcd',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproductpack',
            name='invalid',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproductpack',
            name='qty_uomcd',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='virtualmedicinalproductpack',
            name='vppid',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='virtualtherapeuticmoiety',
            name='invalid',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualtherapeuticmoiety',
            name='vtmid',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
