from django.db import models

# Создание динамической модели.
class City(models.Model):
    # Создание полей модели:
    # name - название города, с максимальной длинной 30.
    name = models.CharField(max_length=30)
    # id - id города на сайте openweathermap.org, который не повторяется и не может иметь значение NUll.
    id = models.IntegerField(primary_key=True, default=0, editable=True)
    # temperature - температура города, изменяющаяся при каждой перезагрузке.
    temperature = models.IntegerField(default=0, editable=True)
    # icon - изображение погоды в городе, изменяющаяся при каждой перезагрузке.
    icon = models.ImageField(default=0, editable=True)
    # Вывод строки вместо объекта для каждого поля.
    def __str__(self):
        return self.name
        return self.id
        return self.temperature
        return self.icon




