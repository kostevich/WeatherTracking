
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from datetime import datetime, timedelta
from django.shortcuts import render
from dublib.Methods import ReadJSON
from .forms import CityForm
from .models import City


import requests

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#
Settings = ReadJSON("main\Settings.json")

#==========================================================================================#
# >>>>> ГЛАВНАЯ СТРАНИЦА <<<<< #
#==========================================================================================#

def main_page(request):
    # Делаем Api-запрос к https://openweathermap.org/.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + Settings["appid"]

    # Переменная cities, отвечающая за вывод объектов класса City.
    cities = City.objects.all()

    # Переменная отвечающая за вывод названия, температуры и иконки города, при его вызове в форме.
    Name = None
    Temperature = None
    Icon = None

    # Если пришёл POST-запрос.
    if request.method == 'POST':
        # Формируем форму в которой отображается название города в виде строчки html.
        form = CityForm(request.POST)
        # Сохранение формы.
        form.save()

        # Получение в json формате данных по погоде в выбранном в форме городе.
        res = requests.get(url.format(request.POST.get('name'))).json()

        # Вывод названия города, записанного в форме пользователем.
        re_name = str(request.POST.get('name'))

        # Фильтр города без id (т.к в форме только имя, значение id default=0).
        a = City.objects.get(id=0)
        # Изменение в модели поля id, temperature, icon (такого же как на https://openweathermap.org/).
        a.id = int(res["id"])
        a.temperature = res["main"]["temp"]
        a.icon = res["weather"][0]["icon"]

        # Дополнение формы данными a.
        form = CityForm(request.POST, instance=a)
        # Удаление объекта, где присутствует только название города.
        City.objects.filter(id=0).delete()
        # Сохранение формы.
        form.save()

        # Итерация объектов модели City.
        for city in cities:
            # Если имя заданного города совпадает с объектом модели City.
            if str(city) == re_name:
                # То получаем значение названия, температуры и иконки города из базы данных.
                Temperature = city.temperature
                Icon = city.icon
                Name = city.name

    # Итерация объектов модели City
    for city in cities:
        # Получение в json формате данных по погоде всех городов по отдельности.
        edit_temperature = requests.get(url.format(city)).json()

        # Итерируем нужный нам объект, для преобразования его в необходимый формат.
        for a in City.objects.filter(name=city):
            # Если температура в базе данных такая же как и на https://openweathermap.org/ для выбранного города.
            if int(edit_temperature["main"]["temp"]) == a.temperature:
                # Приведение даты и времени к сокращенному формату без миллисекунд.
                datetimenow = datetime.now().isoformat(timespec='seconds', sep=' ')

                # Выведение информации об актуальности данных и время последнего обновления.
                updating_information = f'{datetimenow}'
            else:
                # Обновление полей температуры и последнего изменения в базе данных.
                update = City.objects.filter(name=city).update(temperature=edit_temperature["main"]["temp"])
                update = City.objects.filter(name=city).update(updated_at=datetime.now() - timedelta(hours=3))

                # Приведение даты и времени к сокращенному формату без миллисекунд.
                datetimenow = datetime.now().isoformat(timespec='seconds', sep=' ')

                # Выведение информации об актуальности данных и время последнего обновления.
                updating_information = f'{datetimenow}'   

    # Формирование пустой формы.
    form = CityForm()

    # Формируем словарь значения которого: список с названиями городов, температурой и иконкой, и пустая форма, дата и время последнего обновления информации.
    context = {'cities': cities, "form": form, "t": Temperature, "n": Name, "i": Icon, "updating_information": updating_information}
    # Возвращаем страницу html и нужные значения.
    return render(request, "main/MainPage.html", context)
