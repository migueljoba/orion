# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 03:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contribuyentes', '0002_auto_20170326_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContribuyenteTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('F', 'F\xedsico'), ('J', 'Jur\xeddico')], max_length=1, verbose_name='Tipo de contribuyente')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
        ),
        migrations.AddField(
            model_name='contribuyente',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contribuyentes.ContribuyenteTipo'),
        ),
    ]
