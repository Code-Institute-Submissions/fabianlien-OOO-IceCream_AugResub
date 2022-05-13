from django.db import models
from cloudinary.models import CloudinaryField
from colorfield.fields import ColorField
from solo.models import SingletonModel
from django.core.validators import (
    FileExtensionValidator, MaxValueValidator, MinValueValidator)
from django.contrib.auth.models import User

DISPLAY_FLAVOUR = ((0, "Hidden"), (1, "Display"))

# Create your models here.
class About(SingletonModel):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=120)
    image = CloudinaryField(
        'image',
        default=None,
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg"])]
        )

    class Meta:
        verbose_name_plural = 'About Statement'

    def __str__(self):
        return 'About statement'


class MenuPDF(SingletonModel):
    pdf = models.FileField(
        upload_to='static/pdf/',
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
        )

    class Meta:
        verbose_name_plural = 'Upload PDF Menu'

    def __str__(self):
        return 'Menu (.pdf)'


class Flavour(models.Model):
    name = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20)
    description = models.TextField(max_length=120)
    color = ColorField(default='#FF0000')
    allergens = models.TextField(max_length=60)
    display_flavour = models.IntegerField(choices=DISPLAY_FLAVOUR, default=0)
    order_ranking = models.IntegerField(default=1, validators=[
        MaxValueValidator(1000),
        MinValueValidator(1)
    ])

    class Meta:
        ordering = ['order_ranking', 'name']

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.BigIntegerField(unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)
    address = models.CharField(max_length=60, blank=True)
    image = CloudinaryField('image', default='placeholder')
    order_ranking = models.IntegerField(default=100, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])

    class Meta:
        ordering = ['order_ranking', 'name']

    def __str__(self):
        return f'{self.name}'
