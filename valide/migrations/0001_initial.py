# Generated by Django 4.2.8 on 2023-12-20 13:22

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('license', models.CharField(max_length=20)),
                ('manufacture_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2000, 1, 1))])),
                ('plate_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid plate number.', regex='^RA[A-H]{1}\\d{3}[A-Z]$|^(RNP|RDF)\\d{3}[A-Z]$|^(IT|GR|GP|\\w{1,6})$')])),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('mid_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator('@ur\\.ac\\.rw$')])),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number starting with +250 and followed by  9 digits.', regex='^\\+250\\d{1,9}$')])),
                ('date_of_birth', models.DateField()),
                ('reference_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(99), django.core.validators.MaxValueValidator(999)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='valide.vehicle')),
            ],
        ),
    ]