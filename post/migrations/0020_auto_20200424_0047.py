# Generated by Django 3.0.5 on 2020-04-23 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_auto_20200423_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 19, 17, 39, 143260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 19, 17, 39, 142044, tzinfo=utc)),
        ),
    ]