# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0011_auto_20150704_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adicion',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
