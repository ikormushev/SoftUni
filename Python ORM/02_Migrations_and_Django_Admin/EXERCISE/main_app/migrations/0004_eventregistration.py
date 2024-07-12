# Generated by Django 5.0.4 on 2024-07-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_migrate_unique_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=60)),
                ('participant_name', models.CharField(max_length=50)),
                ('registration_date', models.DateField()),
            ],
        ),
    ]
