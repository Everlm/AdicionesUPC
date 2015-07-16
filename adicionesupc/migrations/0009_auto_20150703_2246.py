# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0008_auto_20150703_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='primer_apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='primer_nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre',
            field=models.CharField(null=True, blank=True, max_length=50, default='No tiene'),
        ),
    ]
