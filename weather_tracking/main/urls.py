# Импортируем path для создания необходимого пути к сайту.
from django.urls import path
# Импортируем views для создания наполнения сайта.
from . import views

# Связываем путь к странице и наполнение  страницы.
urlpatterns = [
    path('main_page', views.main_page, name="main page")
]
