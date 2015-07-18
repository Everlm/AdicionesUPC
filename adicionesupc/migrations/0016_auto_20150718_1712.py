# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adicionesupc', '0015_estudiante_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('codigo', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='programa',
            name='facultad',
            field=models.ForeignKey(default='', to='adicionesupc.Facultad'),
            preserve_default=False,
        ),
    ]
