# Generated by Django 2.1.1 on 2018-09-26 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0004_auto_20180926_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagemodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 45, 51, 923301), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='stagemodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 45, 51, 923301), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='stagemodel',
            name='updater',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 45, 51, 923301), verbose_name='更新者'),
        ),
    ]
