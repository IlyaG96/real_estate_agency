from django.db import migrations, models
import phonenumber_field.modelfields
import phonenumbers
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


def add_flat_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().only('owner', 'id')
    for flat in flats:
        owners = Owner.objects.filter(flat_owner=flat.owner)
        for owner in owners:
            owner.flats.set([flat.id])
            owner.save()


def is_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().only('new_building', 'construction_year'):
        flat.new_building = flat.construction_year >= 2015
        flat.save()


def add_owners_to_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().only('owner', 'owners_phonenumber', 'owner_pure_number')
    for flat in flats:
        Owner.objects.get_or_create(
            flat_owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_number=flat.owner_pure_number
        )


def serialize_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().only('owners_phonenumber', 'owner_pure_number'):
        number = flat.owners_phonenumber
        number_to_serialize = phonenumbers.parse(number, 'RU')
        if phonenumbers.is_valid_number(number_to_serialize):
            flat.owner_pure_number = phonenumbers.format_number(number_to_serialize, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]
    operations = [

        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_owner', models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Номер владельца')),
                ('flats', models.ManyToManyField(db_index=True, related_name='flats_in_own', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),

        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
            options={
                'verbose_name': 'Жалоба',
                'verbose_name_plural': 'Жалобы',
            },
        ),

        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(verbose_name='Новостройка'),
        ),

        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Лайкнули')),

        migrations.AddField(
            model_name='flat',
            name='owner_pure_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Номер владельца'),
        ),
        migrations.RunPython(is_new_building),
        migrations.RunPython(serialize_number),
        migrations.RunPython(add_owners_to_model),
        migrations.RunPython(add_flat_to_owner),
    ]
