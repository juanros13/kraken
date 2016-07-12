# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.IntegerField()),
                ('cp', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('clave_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=450)),
                ('nombre_abreviacion', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_municipio', models.IntegerField()),
                ('nombre', models.CharField(max_length=450)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poblacion.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('clave_pais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=450)),
                ('nombre_abreviacion', models.CharField(max_length=450)),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poblacion.Pais'),
        ),
        migrations.AddField(
            model_name='colonia',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poblacion.Estado'),
        ),
    ]
