# Generated by Django 3.2.6 on 2021-09-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20210912_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_id',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate_number',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]