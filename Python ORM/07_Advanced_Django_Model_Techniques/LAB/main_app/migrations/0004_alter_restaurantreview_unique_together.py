# Generated by Django 5.0.4 on 2024-07-18 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_restaurantreview'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='restaurantreview',
            unique_together={('reviewer_name', 'restaurant')},
        ),
    ]
