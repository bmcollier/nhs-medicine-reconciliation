# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20141022_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralPractitioner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=patient.models.generate_first_name, max_length=255)),
                ('last_name', models.CharField(default=patient.models.generate_last_name, max_length=255)),
                ('street', models.CharField(default=patient.models.generate_street, max_length=255)),
                ('town', models.CharField(default=patient.models.generate_town, max_length=255)),
                ('county', models.CharField(default=patient.models.generate_county, max_length=255)),
                ('post_code', models.CharField(default=patient.models.generate_postcode, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(default='M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
    ]
