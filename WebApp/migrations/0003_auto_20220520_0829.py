# Generated by Django 3.2.13 on 2022-05-20 08:29

import cloudinary.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_alter_nybro23text_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg'])], verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='nybro23image',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg'])], verbose_name='image'),
        ),
    ]