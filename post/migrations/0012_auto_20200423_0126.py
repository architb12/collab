# Generated by Django 3.0.5 on 2020-04-22 19:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20200423_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 19, 56, 39, 513771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 19, 56, 39, 513424, tzinfo=utc)),
        ),
    ]
