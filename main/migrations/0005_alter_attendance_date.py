# Generated by Django 4.2.4 on 2024-02-26 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_operation_date_alter_operation_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.timezone, verbose_name='date'),
        ),
    ]