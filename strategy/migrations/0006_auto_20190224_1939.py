# Generated by Django 2.1.7 on 2019-02-25 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0005_testplan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationtype',
            options={'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
        migrations.AlterModelOptions(
            name='browser',
            options={'verbose_name': 'browser', 'verbose_name_plural': 'browsers'},
        ),
        migrations.AlterModelOptions(
            name='mobileso',
            options={'verbose_name': 'mobile', 'verbose_name_plural': 'mobiles'},
        ),
        migrations.AlterModelOptions(
            name='techniquetest',
            options={'verbose_name': 'technique', 'verbose_name_plural': 'techniques'},
        ),
        migrations.AlterModelOptions(
            name='tool',
            options={'verbose_name': 'tool', 'verbose_name_plural': 'tools'},
        ),
        migrations.RenameField(
            model_name='techniquetest',
            old_name='type',
            new_name='tool',
        ),
    ]