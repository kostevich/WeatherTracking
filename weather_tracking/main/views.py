from django.shortcuts import render
from .apikey import appid
import requests
def main_page(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'London'
    res = requests.get(url.format(city)).json()
    city_info = {"city": city, "temp": res["main"]["temp"], "icon": res["weather"][0]["icon"]}
    context = {"info": city_info}
    return render(request, "main/main_page.html", context)
