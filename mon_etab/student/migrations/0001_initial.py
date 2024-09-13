# Generated by Django 5.1 on 2024-09-13 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('absence_date', models.DateTimeField(auto_now_add=True)),
                ('absence_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('reference', models.CharField(max_length=255)),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('expiration_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('birthday', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('url_picture', models.CharField(max_length=255)),
                ('matricule', models.CharField(max_length=255)),
                ('phone_number_father', models.CharField(max_length=255)),
                ('adresse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_person_adress_ids', to='base.adresse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
