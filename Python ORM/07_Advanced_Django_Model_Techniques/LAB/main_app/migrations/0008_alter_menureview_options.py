# Generated by Django 5.0.4 on 2024-07-18 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_menureview_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menureview',
            options={'ordering': ['-rating'], 'verbose_name': 'Menu Review', 'verbose_name_plural': 'Menu Reviews'},
        ),
    ]
