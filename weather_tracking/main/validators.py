from .models import City

def validate_unique(value):
    for city in City.objects.all():
        if value == city.name:
            print(99098)