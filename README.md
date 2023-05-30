# **Weather_tracking**
## Обзор. 
**Weather_tracking** -  веб-сайт, осуществляющий поиск погоды в заданном городе (на базе [openweathermap.org](https://openweathermap.org/)),
имеется автоматически пополняемая база данных о погоде в различных городах.
##  Условия для использования продукта.
1. Установить Python версии не старше [3.11](https://www.python.org/downloads/).

2. В среду исполнения инсталлировать пакет _Django_.:

**`pip install Django`**

3. Получить бесплатный ключа API:

3.1 Зарегистрироваться на сайте [openweathermap.org](https://openweathermap.org/).

3.2 После регистрации нажмите в верхней части страницы _«Ключи API»_.

3.3 Скопировать ключ API.

4. **_Вставить ключ API_** в любой текстовый редактор и назвать его **_apikey_** и сохранить в **_папке main_** этого проекта.

5. Запустить работу сервера командой **```python manage.py runserver```**.

6. Перейти по ссылке указанной после команды.

7. В ссылке открытой в браузере добавьте **_/main_page_**.
____
## Пример работы
Форма для поиска погоды в заданном городе.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/92b789f6-ab64-4a97-aba4-abf2a477afd2)

Информация о погоде в городе, который последним искали.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/c6ff7702-615d-45d1-aefd-337702773f41)

Информация о разных городах, обновляемая, данные сортируются в соответствии с временем поиска.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/25abb70a-42df-4304-9a74-bf025a08ee4f)

Общий вид сайта.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/510f2eac-67e3-4cdc-a94b-65a428fd428e)

База данных сайта.

![image](https://github.com/kostevich/weather_tracking/assets/109979502/11ad2059-ee65-43ee-9bcd-d8cc9a3c7c62)




