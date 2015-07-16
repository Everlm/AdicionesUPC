# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('grupo', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Adiciones',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('codigo', models.CharField(primary_key=True, max_length=12, serialize=False)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('codigo', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(to='adicionesupc.Programa'),
        ),
        migrations.AddField(
            model_name='adicion',
            name='estudiante',
            field=models.ForeignKey(to='adicionesupc.Estudiante'),
        ),
        migrations.AddField(
            model_name='adicion',
            name='materia',
            field=models.ForeignKey(to='adicionesupc.Materia'),
        ),
    ]
