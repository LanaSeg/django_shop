from django.contrib import admin
from app_catalog.models import Category, CategoryIcons
from app_products.models import Product


@admin.register(CategoryIcons)
class CategoryImageAdmin(admin.ModelAdmin):

    list_display = ['pk', 'alt', 'category']
    list_display_links = ['pk', 'alt']


class ImageCategory(admin.TabularInline):
    model = CategoryIcons


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ImageCategory]
    list_display = ['pk', 'title', 'parent', 'active', 'favourite']
    list_display_links = ['pk', 'title']
    list_filter = ['parent', 'active', 'favourite']
    search_fields = ['title']
    ordering = ['parent', 'active']
    actions = ['make_active', 'make_inactive', 'make_favourite', 'make_not_favourite']

    @admin.action(description='Сделать активной')
    def make_active(self, request, category):
        updated = category.update(active=True)
        self.message_user(request, message=f'Активные категории: {updated}')

    @admin.action(description='Сделать неактивной')
    def make_inactive(self, request, category):
        updated = category.update(active=False)
        Product.objects.filter(category__in=category).update(active=False)
        self.message_user(request, message=f'Неактивные категории: {updated}')

    @admin.action(description='Сделать избранной')
    def make_favourite(self, request, category):
        updated = category.update(favourite=True)
        self.message_user(request, message=f'Избранные категории: {updated}')