from rest_framework import serializers
from app_catalog.models import Category, CategoryIcons
from app_products.models import Tag

""" Сериализация банеров, категорий и подкатекорий, иконок, тегов """


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'href', 'price', 'images']
    price = serializers.StringRelatedField()
    images = serializers.StringRelatedField(many=True)


class CategoryIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryIcons
        fields = ['src', 'alt']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']
    image = CategoryIconsSerializer(many=False, read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']
    image = CategoryIconsSerializer(many=False, read_only=True)
    subcategories = SubCategorySerializer(many=True, read_only=True)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['product']


