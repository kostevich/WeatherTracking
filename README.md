# **WeatherTracking**
**WeatherTracking** – учебный проект на [Django](https://github.com/django/django), осуществляющий поиск погоды в заданном городе (на базе [OpenWeatherMap](https://openweathermap.org/)),
имеется автоматически пополняемая база данных о погоде в различных городах.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать.
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: dublib(https://github.com/DUB1401/dublib), [Django](https://github.com/django/django?ysclid=lph3fmn0za256973455) не старше 4.2.1, [requests](https://github.com/psf/requests?ysclid=lpv45zob9i45918043)
```
pip install git+https://github.com/DUB1401/dublib#egg=dublib
pip install Django
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. Получить бесплатный ключ API на сайте [OpenWeatherMap](https://openweathermap.org/).
5. Cкопировать полученный API-ключ в файл  _apikey.py_ в папке _weather_tracking/main/apikey.py_.
   
   Пример: appid = 'c6d52e8ad0ebe7dffb7ea4567ec63'
7. В среде исполнения запустить файл _manage.py_ командой:
```
python manage.py runserver
```
8. Перейти по ссылке (пример: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

# Отслеживание данных в адмиистративной панели Django.
1. В среде исполнения запустить команду:
```
python manage.py createsuperuser
```
2. Зарегистрироваться.
3. Перейти по ссылке добавив к ней admin (пример: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)).

# Отслеживание в базе данных.
Откройте файл db.sqlite3 в программе для открытия баз данных (пример: [SQLiteStudio](https://sqlitestudio.pl/)).

# Пример работы
**Форма для поиска погоды в заданном городе**:

![image](https://github.com/kostevich/weather_tracking/assets/109979502/92b789f6-ab64-4a97-aba4-abf2a477afd2)

**Информация о погоде в последнем искомом городе**:

![image](https://github.com/kostevich/weather_tracking/assets/109979502/c6ff7702-615d-45d1-aefd-337702773f41)

**Перечень данных о погоде в искомых городах**:

![image](https://github.com/kostevich/weather_tracking/assets/109979502/25abb70a-42df-4304-9a74-bf025a08ee4f)

**Общий вид сайта**:

![image](https://github.com/kostevich/weather_tracking/assets/109979502/510f2eac-67e3-4cdc-a94b-65a428fd428e)

**База данных сайта**:

![image](https://github.com/kostevich/weather_tracking/assets/109979502/11ad2059-ee65-43ee-9bcd-d8cc9a3c7c62)

_Copyright © Kostevich Irina. 2023._
