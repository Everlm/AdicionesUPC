# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0005_auto_20150701_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='primer_nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='No deben haber numeros', regex='^[a-zA-Z]$')]),
        ),
    ]
