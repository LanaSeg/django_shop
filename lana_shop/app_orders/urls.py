from . import routers
from app_orders.views import OrdersView, PaymentView
from django.urls import path

app_name = 'app_orders'

router = routers.MyRouter()
router.register(r'api/orders', OrdersView)

urlpatterns = [
    path("api/payment/", PaymentView.as_view()),
] + router.urls
