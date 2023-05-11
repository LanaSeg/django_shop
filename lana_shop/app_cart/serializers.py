from rest_framework import serializers
from app_products.models import Product
from decimal import Decimal


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    count = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    href = serializers.StringRelatedField()
    images = serializers.StringRelatedField(many=True)

    def get_count(self, obj):
        return self.context.get(str(obj.pk)).get('count')

    def get_price(self, obj):
        return Decimal(self.context.get(str(obj.pk)).get('price'))
