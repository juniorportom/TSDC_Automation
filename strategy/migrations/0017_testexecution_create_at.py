# Generated by Django 2.1.7 on 2019-03-18 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0016_testexecution_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexecution',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
