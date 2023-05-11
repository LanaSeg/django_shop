from rest_framework import serializers
import locale
from app_products.models import Product, ProductSpecification, Reviews, Tag, Sale
import datetime

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        exclude = ['id', 'product']
    specification_name = serializers.StringRelatedField()
    name = serializers.StringRelatedField()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['author', 'email', 'text', 'rate', 'date', 'product']
    date = serializers.SerializerMethodField()

    def get_date(self, instance):
        date = instance.date + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(date, '%d.%m.%Y %H:%M')


class TagsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['limited_edition']
    images = serializers.SerializerMethodField()
    description = serializers.StringRelatedField()
    tags = TagsProductSerializer(many=True, required=False)
    specifications = SpecificationsSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)
    href = serializers.StringRelatedField()
    photoSrc = serializers.SerializerMethodField()
    categoryName = serializers.StringRelatedField()
    price = serializers.SerializerMethodField()
    id = serializers.IntegerField()

    def get_photoSrc(self, instance):
        src = [str(instance.images.first())]
        return src

    def get_images(self, instance):
        images = []
        images_tmp = instance.images.all()
        for image in images_tmp:
            images.append(image.__str__())
        return images

    def get_price(self, instance):
        salePrice = instance.sales.first()
        if salePrice:
            return salePrice.salePrice
        return instance.price


class SaleSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    title = serializers.StringRelatedField()
    href = serializers.StringRelatedField()
    price = serializers.StringRelatedField()
    dateFrom = serializers.DateField(format='%d.%b')
    dateTo = serializers.DateField(format='%d.%b')

    class Meta:
        model = Sale
        fields = '__all__'
