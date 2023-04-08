from django.db import models
from cloudinary.models import CloudinaryField
from config.constants import *


class Item(models.Model):
    class Meta(object):
        db_table = 'item'

    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    COLOR_CHOICES = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    )

    status = models.CharField(
        'status', blank=False, default='inactive', max_length=50, db_index=True, choices=STATUS
    )

    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
    )

    price = models.DecimalField(
        'price', blank=False, null=False, max_digits=14, decimal_places=2
    )

    size = models.CharField(
        'Size', blank=True, null=True, max_length=1, choices=SIZE_CHOICES
    )

    color = models.CharField(
        'Color', blank=True, null=True, max_length=10, choices=COLOR_CHOICES
    )

    image = CloudinaryField(
        'image', blank=False, null=False
    )

    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name
