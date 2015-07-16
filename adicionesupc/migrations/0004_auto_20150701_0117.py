# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0003_remove_materia_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='segundo_nombre',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]
