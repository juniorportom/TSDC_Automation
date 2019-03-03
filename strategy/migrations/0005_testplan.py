# Generated by Django 2.1.7 on 2019-02-25 00:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0004_teststrategy'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('script_file', models.FileField(blank=True, null=True, upload_to='scripts/')),
                ('execution_date', models.DateTimeField(default=datetime.datetime.now)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('browser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Browser')),
                ('mobile_so', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.MobileSO')),
                ('technique_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.TechniqueTest')),
                ('test_strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.TestStrategy')),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'tests',
                'ordering': ['-create_at'],
            },
        ),
    ]
