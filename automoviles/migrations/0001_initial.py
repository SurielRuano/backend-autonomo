# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('anio', models.DateField(auto_now=True)),
                ('doors_num', models.IntegerField()),
                ('cylinders_num', models.IntegerField()),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('img_front', models.ImageField(blank=True, null=True, upload_to='assets')),
                ('img_left', models.ImageField(blank=True, null=True, upload_to='assets')),
                ('img_right', models.ImageField(blank=True, null=True, upload_to='assets')),
                ('img_back', models.ImageField(blank=True, null=True, upload_to='assets')),
                ('car_line', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
    ]
