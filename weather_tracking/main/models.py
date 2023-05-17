from django.db import models

# Create model City for output cities.
class City(models.Model):
    # Output of the name of the city with a length restriction.
    name = models.CharField(max_length=30)
    id = models.CharField(primary_key=True, unique=True, max_length=20, default=0, editable=True)
    temperature = models.CharField(max_length=10, default=0, editable=True)
    icon = models.ImageField(default=0, editable=True)
    # Output str instead of the object.
    def __str__(self):
        # Output str of the name of the city instead of the object.
        return self.name
        return self.id




