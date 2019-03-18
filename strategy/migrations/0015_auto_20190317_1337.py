# Generated by Django 2.1.7 on 2019-03-17 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0014_auto_20190316_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexecution',
            name='browser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Browser'),
        ),
        migrations.AddField(
            model_name='testexecution',
            name='executed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testexecution',
            name='mobile_so',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.MobileSO'),
        ),
        migrations.AddField(
            model_name='testexecution',
            name='script',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.ApplicationScript'),
        ),
    ]
