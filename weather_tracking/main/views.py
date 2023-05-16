from django.shortcuts import render
from .apikey import appid
from .models import City
import requests
from .forms import CityForm


def main_page(request):
    # Делаем Api-запрос к стороннему сайту.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    # Переменная cities, отвечающая за вывод объектов класса City (Содержится только название города).
    cities = City.objects.all()
    # Создаем  пустой список.
    all_cities = []
    # Если был выбран метод post.
    if request.method == 'POST':
        # Формируем форму в которой отображается название города в виде строчки html.
        form = CityForm(request.POST)
        # Сохранение формы.
        form.save()

    # Формирование пустой формы.
    form = CityForm
    # Итерируем все объекты класса City (только название).
    for city in cities:
        # Посылаем запрос к стороннему сайту, получаем в формате json.
        res = requests.get(url.format(city.name)).json()
        # Формируем словарь с ключами: название, температура, иконка.
        city_info = {"city": city.name, "temp": res["main"]["temp"], "icon": res["weather"][0]["icon"], "id": res["id"]}
        list_city_info = []
        list_city_info.append(city_info)
        # Добавляем словарь в список с названиями городов, температурой и иконкой.
        all_cities.append(city_info)
    try:
        t = City.objects.get(id=0)
        t.id = int(res["id"])
        t.save()
        City.objects.filter(id=0).delete()
    except City.DoesNotExist:
        print(0)
    # Формируем словарь значения которого: список с названиями городов, температурой и иконкой, и пустая форма.
    context = {"all_info": all_cities, "form": form, "list_city_info": list_city_info}
    # Возвращаем страницу html и нужные значения.
    return render(request, "main/main_page.html", context)
