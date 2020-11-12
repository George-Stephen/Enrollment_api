# Generated by Django 3.1.3 on 2020-11-12 09:06

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('id_number', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('front_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('back_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
