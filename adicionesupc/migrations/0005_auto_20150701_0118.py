# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0004_auto_20150701_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre',
            field=models.CharField(max_length=50, blank=True, default='No tiene', null=True),
        ),
    ]
