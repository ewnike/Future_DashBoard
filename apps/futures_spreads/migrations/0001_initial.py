# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Future',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('symbol', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('back', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_month', to='futures_spreads.Future')),
                ('front', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front_month', to='futures_spreads.Future')),
            ],
        ),
    ]
