# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0014_auto_20150715_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='correo',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
