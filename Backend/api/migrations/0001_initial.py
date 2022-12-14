# Generated by Django 4.1.1 on 2022-10-01 21:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatiPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('F', 'Femmina'), ('M', 'Maschio')], max_length=1)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(max_length=200)),
                ('codice_fiscale', models.CharField(blank=True, max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(16)])),
            ],
        ),
    ]
