from django.db import models
from django import forms

def validate_unique(value):
    for city in City.objects.all():
        if value == city.name:
            raise ValueError('ferf')

# Create model City for output cities.
class City(models.Model):
    # Output of the name of the city with a length restriction.
    name = models.CharField(max_length=30, validators=[validate_unique])
    # Output str instead of the object.
    def __str__(self):
        # Output str of the name of the city instead of the object.
        return self.name

