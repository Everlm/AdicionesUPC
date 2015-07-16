# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0007_auto_20150703_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='codigo',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
