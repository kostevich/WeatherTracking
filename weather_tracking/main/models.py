# Импортируем models для работы с моделями.
from django.db import models


# Создание модели City.
class City(models.Model):
    # Создание полей модели: name - название города, с максимальной длинной 30.
    name = models.CharField(max_length=30)
    # id - id города на сайте openweathermap.org, который не повторяется, по умолчанию 0, можно изменять.
    id = models.IntegerField(primary_key=True, default=0, editable=True)
    # temperature - температура города, изменяющаяся при каждоом изменении на openweathermap.org, по умолчанию 0.
    temperature = models.IntegerField(default=0, editable=True)
    # icon - изображение погоды в городе, изменяющаяся при каждом изменении на openweathermap.org, по умолчанию 0.
    icon = models.ImageField(default=0, editable=True)
    # created_at - дата и время создания записи, добавляется самостоятельно, может иметь значение 0.
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # updated_at - дата и время изменения в базе данных записи, может иметь значение 0.
    updated_at = models.DateTimeField(auto_now=True, editable=True, null=True)

    # Класс Meta, конструирующий class City.
    class Meta:
        # Вывод информации в порядке позднего - раннего изменения поля updated_at.
        ordering = ['-updated_at']

    # Вывод строки вместо объекта для каждого поля.
    def __str__(self):
        return self.name
