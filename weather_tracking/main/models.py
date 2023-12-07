
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.db import models

#==========================================================================================#
# >>>>> МОДЕЛЬ: ОПИСАНИЕ ГОРОДА <<<<< #
#==========================================================================================#

class City(models.Model):
    # Создание полей модели.
    name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True, default=0, editable=True)
    temperature = models.IntegerField(default=0, editable=True)
    icon = models.ImageField(default=0, editable=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True, null=True)

    # Сортировка по полю updated_at.
    class Meta:
        ordering = ['-updated_at']

    # Строковый вид поля name.
    def __str__(self):
        return self.name
