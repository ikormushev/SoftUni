# Generated by Django 5.0.4 on 2024-07-10 22:14

from django.db import migrations


def set_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')
    people = person.objects.all()

    for p in people:
        if p.age <= 12:
            p.age_group = 'Child'
        elif p.age <= 17:
            p.age_group = 'Teen'
        else:
            p.age_group = 'Adult'
        p.save()


def reverse_set_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')
    people = person.objects.all()

    for p in people:
        p.age_group = person._meta.get_field('age_group').default
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [
        migrations.RunPython(set_age_group, reverse_code=reverse_set_age_group)
    ]
