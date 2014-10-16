# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital_id', models.CharField(default=b'14134743445', unique=True, max_length=100, editable=False)),
                ('nhs_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{3} [0-9]{3} [0-9]{4}', message=b'NHS Number must be in the format 000 000 0000')])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
