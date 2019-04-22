# Generated by Django 2.1.7 on 2019-04-15 00:22

from django.db import migrations, models
import django.db.models.deletion
import strategy.models.stepImage


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0018_techniquetest_function_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=strategy.models.stepImage.custom_upload_to)),
                ('test_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.TestExecution')),
            ],
            options={
                'verbose_name': 'image_step',
                'verbose_name_plural': 'image_steps',
            },
        ),
    ]
