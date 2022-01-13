# Generated by Django 2.2.24 on 2022-01-13 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_serialize_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_owner', to='property.Flat', verbose_name='ФИО владельца')),
                ('flats', models.ManyToManyField(related_name='flats', to='property.Flat', verbose_name='Квартиры в собственности')),
                ('owner_pure_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_pure_phonenumber', to='property.Flat', verbose_name='Нормализованный номер владельца')),
                ('owners_phonenumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_phonenumber', to='property.Flat', verbose_name='Номер владельца')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
