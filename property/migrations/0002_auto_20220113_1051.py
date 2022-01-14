# Generated by Django 2.2.24 on 2022-01-13 07:40

from django.db import migrations


def move_users(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().only('owner', 'owners_phonenumber', 'owner_pure_number')
    for flat in flats:
        Owner.objects.get_or_create(
            flat_owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_number=flat.owner_pure_number
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(move_users)
    ]