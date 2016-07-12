# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 09:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poblacion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(default=None)),
                ('visto', models.BooleanField(default=0)),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('fecha_modificacion', models.DateTimeField(editable=False)),
                ('usuario_envia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_crea', to=settings.AUTH_USER_MODEL)),
                ('usuario_recibe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_entrega', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(blank=True, default=None, max_length=21, null=True)),
                ('telefono', models.CharField(blank=True, default=None, max_length=21, null=True)),
                ('celular', models.CharField(blank=True, default=None, max_length=21, null=True)),
                ('rfc', models.CharField(blank=True, default=None, max_length=18, null=True)),
                ('razon_social', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('avatar', models.FileField(upload_to=b'avatars/%Y/%m/%d')),
                ('colonia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poblacion.Colonia')),
                ('estado', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poblacion.Estado')),
                ('municipio', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poblacion.Municipio')),
                ('pais', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poblacion.Pais')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
