# Generated by Django 3.0.5 on 2020-05-03 18:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0035_auto_20200503_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 18, 17, 14, 338350, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 18, 17, 14, 337311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 18, 17, 14, 339425, tzinfo=utc)),
        ),
    ]
