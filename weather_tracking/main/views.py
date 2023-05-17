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
        form = CityForm()
        # Переменная cities, отвечающая за вывод объектов класса City (Содержится только название города).
        cities = City.objects.all()
        # Итерируем все объекты класса City (только название).
        for city in cities:
            # Посылаем запрос к стороннему сайту, получаем в формате json.
            res = requests.get(url.format(city.name)).json()
        try:
            t = City.objects.get(id=0)
            t.city = city.name
            t.id = int(res["id"])
            t.temperature = res["main"]["temp"]
            t.icon = res["weather"][0]["icon"]
            t.save()
            City.objects.filter(id=0).delete()
        except City.DoesNotExist:
            print(0)
    # Формируем словарь значения которого: список с названиями городов, температурой и иконкой, и пустая форма.
    context = {'cities': cities, "form": form}
    # Возвращаем страницу html и нужные значения.
    return render(request, "main/main_page.html", context)



