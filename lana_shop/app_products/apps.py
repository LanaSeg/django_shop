from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_products'
    verbose_name = 'продукт'
    verbose_name_plural = 'продукты'
