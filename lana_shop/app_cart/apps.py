from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_cart'
    verbose_name = 'корзина'
    verbose_name_plural = 'корзины'
