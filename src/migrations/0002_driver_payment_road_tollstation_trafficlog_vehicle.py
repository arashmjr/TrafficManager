# Generated by Django 3.2.6 on 2021-08-07 05:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('birthdate', models.IntegerField(blank=True, null=True)),
                ('national_code', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('road_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('origin', models.CharField(max_length=40)),
                ('destination', models.CharField(max_length=40)),
                ('minimum_height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(blank=True, max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('weight', models.BigIntegerField()),
                ('height', models.IntegerField()),
                ('model', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.driver')),
            ],
        ),
        migrations.CreateModel(
            name='TrafficLog',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(max_length=30)),
                ('vehicle_color', models.CharField(blank=True, max_length=30)),
                ('road_width', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('province_name', models.CharField(max_length=30)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField()),
                ('road_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.road')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='TollStation',
            fields=[
                ('toll_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('heavy_vehicle_charge', models.IntegerField()),
                ('light_vehicle_charge', models.IntegerField()),
                ('heavy_vehicle_charge_per_kg', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField()),
                ('road_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.road')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=30)),
                ('road_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.road')),
                ('toll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.tollstation')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.vehicle')),
            ],
        ),
    ]
