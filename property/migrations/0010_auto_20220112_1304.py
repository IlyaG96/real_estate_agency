# Generated by Django 2.2.24 on 2022-01-12 10:04

from django.db import migrations
import phonenumbers


def serialize_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().only('owners_phonenumber', 'owner_pure_number'):
        number_to_serialize = flat.owners_phonenumber
        phonenumbers_obj = phonenumbers.parse(number_to_serialize, "RU")
        flat.owner_pure_number = phonenumbers.format_number(phonenumbers_obj, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220112_1252'),
    ]

    operations = [
        migrations.RunPython(serialize_number)
    ]
