# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0013_auto_20150704_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
