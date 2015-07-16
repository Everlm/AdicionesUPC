# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0009_auto_20150703_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adicion',
            options={'verbose_name_plural': 'Adiciones', 'ordering': ['-fecha']},
        ),
    ]
