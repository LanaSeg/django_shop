from django.urls import path
from app_cart.views import BasketOfProductsView

app_name = 'app_cart'

urlpatterns = [
    path('api/basket/', BasketOfProductsView.as_view(), name='basket'),
    path('api/cart/', BasketOfProductsView.as_view(), name='cart'),
]
