# Generated by Django 5.0.4 on 2024-07-20 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_movies', to='main_app.director'),
        ),
    ]
