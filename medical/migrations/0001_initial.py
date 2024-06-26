# Generated by Django 5.0.6 on 2024-05-15 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=70)),
                ('birth_of_date', models.DateField()),
                ('gender', models.CharField(choices=[('ayol', 'ayol'), ('erkak', 'erkak')], max_length=10)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='person_images/')),
                ('profession', models.CharField(max_length=50)),
                ('person_role', models.CharField(choices=[('ordinary', 'ordinary'), ('doctor', 'doctor')], default='ordinary', max_length=10)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='medical.family')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
