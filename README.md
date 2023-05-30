# **Weather_tracking**
____
## Обзор. 
**Weather_tracking** -  веб-сайт на [Django](https://github.com/django/django), осуществляющий поиск погоды в заданном городе (на базе [OpenWeatherMap](https://openweathermap.org/)),
имеется автоматически пополняемая база данных о погоде в различных городах.
____
##  Условия для использования продукта.
1. Установить Python версии не старше [3.11](https://www.python.org/downloads/).

2. В среду исполнения инсталлировать пакеты **_Django, Pillow_**:

  **`pip install Django`**

  **`pip install Pillow`**

3. Получить бесплатный ключ API на сайте [OpenWeatherMap](https://openweathermap.org/).

4. Cкопировать полученный API-ключ в файл **_apikey.py_** в папке **weather_tracking/main/apikey.py**.

  **Пример: appid = 'c6d52e8ad0ebe7dffb7ea3897ec63'**
  
5. Запустить сервер через терминал, предварительно указав исполняемую директорию методом `cd`.

**```python manage.py runserver```**.

6. Перейти по [ссылке](http://127.0.0.1:8000/main_page).
____
## Пример работы
Форма для поиска погоды в заданном городе.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/92b789f6-ab64-4a97-aba4-abf2a477afd2)

Информация о погоде в последнем искомом городе.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/c6ff7702-615d-45d1-aefd-337702773f41)

Перечень данных о погоде в искомых городах.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/25abb70a-42df-4304-9a74-bf025a08ee4f)

Общий вид сайта.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/510f2eac-67e3-4cdc-a94b-65a428fd428e)

База данных сайта.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/11ad2059-ee65-43ee-9bcd-d8cc9a3c7c62)
