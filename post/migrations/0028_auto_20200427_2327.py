# Generated by Django 3.0.5 on 2020-04-27 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_auto_20200425_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 17, 57, 32, 726810, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 17, 57, 32, 726350, tzinfo=utc)),
        ),
    ]
