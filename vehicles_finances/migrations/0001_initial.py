# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=250)),
                ('amount', models.FloatField()),
                ('observations', models.TextField()),
                ('date_payment', models.DateField()),
                ('reference_payment', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'DetailPayments',
                'verbose_name': 'DetailPayment',
            },
        ),
        migrations.CreateModel(
            name='SettingsFinantial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_factor', models.FloatField()),
                ('administration_fee', models.FloatField()),
                ('inscription_fee', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'SettingsFinantials',
                'verbose_name': 'SettingsFinantial',
            },
        ),
        migrations.CreateModel(
            name='StockExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('maximum_number_customers', models.IntegerField()),
                ('monthly_payment', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'StockExchanges',
                'verbose_name': 'StockExchange',
            },
        ),
        migrations.CreateModel(
            name='VehicleBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('deadline', models.DateField()),
                ('adjudication', models.BooleanField(choices=[(True, 'Adjudicado'), (False, 'No Adjudicado')], default=False)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiclebook', to='clients.Client')),
                ('id_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiclebook', to='vehicles_finances.StockExchange')),
                ('id_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiclebook', to='vehicles.Vehicle')),
            ],
            options={
                'verbose_name_plural': 'VehicleBookings',
                'verbose_name': 'VehicleBooking',
            },
        ),
        migrations.AddField(
            model_name='detailpayment',
            name='id_vehiclebooking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detailpayment', to='vehicles_finances.VehicleBooking'),
        ),
    ]
