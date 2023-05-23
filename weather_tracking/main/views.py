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
    # Если был выбран метод post.
    if request.method == 'POST':
        # Формируем форму в которой отображается название города в виде строчки html.
        form = CityForm(request.POST)
        # Создать экземпляр формы из данных POST.
        form.save()
        res = requests.get(url.format(request.POST.get('name'))).json()
        a = City.objects.get(id=0)
        a.id = int(res["id"])
        a.temperature = res["main"]["temp"]
        a.icon = res["weather"][0]["icon"]
        form = CityForm(request.POST, instance=a)
        City.objects.filter(id=0).delete()
        # Сохранение формы.
        form.save()
    # Формирование пустой формы.
    form = CityForm()
    # Формируем словарь значения которого: список с названиями городов, температурой и иконкой, и пустая форма.
    context = {'cities': cities, "form": form}
    # Возвращаем страницу html и нужные значения.
    return render(request, "main/main_page.html", context)



