# Generated by Django 5.0.4 on 2024-07-18 17:59

import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_hero_flashhero_spiderhero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
            ],
        ),
    ]
