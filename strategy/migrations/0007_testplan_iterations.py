# Generated by Django 2.1.7 on 2019-03-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0006_auto_20190224_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='testplan',
            name='iterations',
            field=models.IntegerField(default=1),
        ),
    ]
