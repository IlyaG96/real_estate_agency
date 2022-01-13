# Generated by Django 2.2.24 on 2022-01-13 13:03

from django.db import migrations


def move_users(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().only('owner', 'id')
    for flat in flats:
        try:
            owner = Owner.objects.get(flat_owner=flat.owner)
            owner.flats.set([flat.id])
            owner.save()
        except Owner.MultipleObjectsReturned:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220114_0212'),
    ]

    operations = [
        migrations.RunPython(move_users)
    ]





