from app_cart.cart import Cart
from app_cart.serializers import BasketSerializer
from app_products.models import Product
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


def get_products_in_cart(cart):
    """ Функция для получения продуктов из корзины и их сериализация """
    products_in_cart = [product for product in cart.cart.keys()]
    products = Product.objects.filter(pk__in=products_in_cart)
    serializer = BasketSerializer(products, many=True, context=cart.cart)
    return serializer


class BasketOfProductsView(APIView):
    """ Получение, добавление, удаления товаров из корзины. """
    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        serializer = get_products_in_cart(cart)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.request.data.get('id'))
        cart.add(product=product, count=self.request.data.get('count'))
        serializer = get_products_in_cart(cart)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.request.query_params.get('id'))
        count = self.request.query_params.get('count', False)
        cart.remove(product, count=count)
        serializer = get_products_in_cart(cart)
        return Response(serializer.data)
