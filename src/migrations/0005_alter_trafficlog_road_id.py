# Generated by Django 3.2.6 on 2021-08-20 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_alter_trafficlog_road_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficlog',
            name='road_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='src.road'),
        ),
    ]
