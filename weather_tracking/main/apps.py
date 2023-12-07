
from django.apps import AppConfig


# Регистрация приложения main.
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Название приложения main.
    name = 'main'
