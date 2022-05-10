from django.db import models
from cloudinary.models import CloudinaryField
from colorfield.fields import ColorField
from solo.models import SingletonModel
from django.contrib.auth.models import User


# Create your models here.
class About(SingletonModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = CloudinaryField('image', default=None)

    def __str__(self):
        return "About statement"


class Flavour(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    color = ColorField(default='#FF0000')
    allergens = models.TextField(max_length=100)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name
