# Generated by Django 2.1.7 on 2019-03-11 05:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import strategy.models.applicationScript


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0009_testexecution'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('script_file', models.FileField(blank=True, null=True, upload_to=strategy.models.applicationScript.custom_upload_to)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Application')),
                ('technique_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.TechniqueTest')),
            ],
            options={
                'verbose_name': 'script',
                'verbose_name_plural': 'scripts',
                'ordering': ['-create_at'],
            },
        ),
        migrations.AlterField(
            model_name='testplan',
            name='browser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Browser'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='mobile_so',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.MobileSO'),
        ),
    ]
