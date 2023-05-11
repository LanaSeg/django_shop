from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_catalog'
    verbose_name = 'каталог'
    verbose_name_plural = 'каталоги'
