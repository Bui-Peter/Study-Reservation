# Generated by Django 2.0.5 on 2018-05-26 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='study_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]