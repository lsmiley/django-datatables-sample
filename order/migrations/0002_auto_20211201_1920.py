# Generated by Django 2.2.10 on 2021-12-02 00:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 1, 19, 20, 36, 946164)),
        ),
    ]
