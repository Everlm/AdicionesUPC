# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programa',
            options={'verbose_name_plural': 'Programas'},
        ),
    ]
