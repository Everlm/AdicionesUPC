# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0002_auto_20150701_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='grupo',
        ),
    ]
