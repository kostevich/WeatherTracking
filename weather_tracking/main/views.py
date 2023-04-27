from django.shortcuts import render
from .apikey import appid
from .models import City
import requests
from .forms import CityForm


def main_page(request):
    # Делаем Api-запрос к стороннему сайту.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    # Если был выбран метод post.
    if request.method == 'POST':
        # Формируем форму в которой отображается название города в виде строчки html.
        form = CityForm(request.POST)
        # Сохранение формы.
        form.save()


    # Формирование пустой формы.
    form = CityForm
    # Переменная cities, отвечающая за вывод объектов класса City (Содержится только название города) .
    cities = City.objects.all()
    # Создаем  пустой список.
    all_cities = []
    # Итерируем все объекты класса City (только название).
    for city in cities:
        # Посылаем запрос к стороннему сайту, получаем в формате json.
        res = requests.get(url.format(city.name)).json()
        # Формируем словарь с ключами: название, температура, иконка.
        city_info = {"city": city.name, "temp": res["main"]["temp"], "icon": res["weather"][0]["icon"]}
        # Добавляем словарь в список с названиями городов, температурой и иконкой.
        all_cities.append(city_info)
    # Формируем словарь значения которого: список с названиями городов, температурой и иконкой, и пустая форма.
    context = {"all_info": all_cities, "form": form}
    # Возвращаем страницу html и нужные значения.
    return render(request, "main/main_page.html", context)
