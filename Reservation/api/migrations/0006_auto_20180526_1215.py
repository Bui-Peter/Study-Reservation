# Generated by Django 2.0.5 on 2018-05-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180526_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_size',
            field=models.IntegerField(choices=[(2, '2'), (4, '4'), (6, '6'), (8, 'eight')]),
        ),
    ]