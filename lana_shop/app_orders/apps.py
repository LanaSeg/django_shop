from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_orders'
    verbose_name = 'заказ'
    verbose_name_plural = 'заказы'
