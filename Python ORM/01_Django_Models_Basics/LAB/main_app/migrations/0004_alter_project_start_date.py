# Generated by Django 5.0.4 on 2024-07-09 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_project_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start Date'),
        ),
    ]
