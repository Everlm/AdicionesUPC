# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0006_auto_20150701_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='codigo',
            field=models.CharField(primary_key=True, max_length=12, validators=[django.core.validators.RegexValidator(message='No deben haber numeros', regex='^[a-zA-Z]$')], serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='primer_apellido',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='No deben haber numeros', regex='^[a-zA-Z]$')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_apellido',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='No deben haber numeros', regex='^[a-zA-Z]$')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre',
            field=models.CharField(default='No tiene', blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='No deben haber numeros', regex='^[a-zA-Z]$')]),
        ),
    ]
