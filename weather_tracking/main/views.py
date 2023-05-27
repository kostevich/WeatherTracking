# Render - импортируем для объединения шаблона html с словарем и возвращения объекта визуализированным текстом.
from django.shortcuts import render
# Appid - импортируем для конфиденциальности Api-ключа с https://openweathermap.org/.
from .apikey import appid
# Модель City - для редактирования ее полей.
from .models import City
# Requests - импортируем для составления HTTP-запросов.
import requests
# Форма CityForm- для ее сохранения.
from .forms import CityForm
# Datetime - импортируем для сохранения времени изменения поля модели.
# Timedelta - импортируем для сохранения времени в одном формате UTC.
from datetime import datetime, timedelta

#& Функция, осуществляющая работу всего сайта.
def main_page(request):
    # Делаем Api-запрос к https://openweathermap.org/.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    # Переменная cities, отвечающая за вывод объектов класса City.
    cities = City.objects.all()
    ### Переменная отвечающая за вывод названия(n), температуры(t) иконки(i) города, при его вызове в форме.
    n = None
    t = None
    i = None
    # Если был выбран метод post.
    if request.method == 'POST':
        # Формируем форму в которой отображается название города в виде строчки html.
        form = CityForm(request.POST)
        # Создание экземпляр формы из данных POST, где содержится в качестве значения только название города.
        form.save()
        # Получение в json формате данных по погоде в выбранном в форме пользователем городе.
        res = requests.get(url.format(request.POST.get('name'))).json()
        # Вывод названия города, записанного в форме пользователем.
        re_name = str(request.POST.get('name'))
        # Фильтр города без id (т.к в форме только имя, значение id default=0).
        a = City.objects.get(id=0)
        ### Изменениние в модели поля id, temperature, icon (такого же как на https://openweathermap.org/).
        a.id = int(res["id"])
        a.temperature = res["main"]["temp"]
        a.icon = res["weather"][0]["icon"]
        form = CityForm(request.POST, instance=a)
        City.objects.filter(id=0).delete()
        # Сохранение формы.
        form.save()
        for city in cities:
            c = str(city)
            if c == re_name:
                t = city.temperature
                i = city.icon
                n = city.name
    for city in cities:
        edit_temperature = requests.get(url.format(city)).json()
        a = City.objects.filter(name=city)
        for a in a:
            a.temperature
            if int(edit_temperature["main"]["temp"]) == a.temperature:
                print(a.temperature)
                print(int(edit_temperature["main"]["temp"]))
                print("изменений нет")
            else:
                update = City.objects.filter(name=city).update(temperature=edit_temperature["main"]["temp"])
                update = City.objects.filter(name=city).update(updated_at=datetime.now() - timedelta(hours=3))
                print(a.temperature)
                print(int(edit_temperature["main"]["temp"]))
                print("изменения есть")
    # Формирование пустой формы.
    form = CityForm()
    # Формируем словарь значения которого: список с названиями городов, температурой и иконкой, и пустая форма.
    context = {'cities': cities, "form": form, "t": t, "n": n, "i": i}
    # Возвращаем страницу html и нужные значения.
    return render(request, "main/main_page.html", context)




