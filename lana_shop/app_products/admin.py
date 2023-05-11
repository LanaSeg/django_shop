from django.contrib import admin
from app_catalog.models import Category
from app_products.models import Product, ProductImage, Tag, Specification, ProductSpecification, Sale


class CategoryOfSpecification(admin.TabularInline):
    model = Specification.category.through


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):

    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
    inlines = [CategoryOfSpecification]
    exclude = ['category']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product']
    list_display_links = ['pk', 'product']


class ProductImages(admin.TabularInline):
    model = ProductImage


class ProductSpecifications(admin.TabularInline):
    model = ProductSpecification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'price',
        'count',
        'category',
        'limited_edition',
        'active'
    ]
    list_display_links = ['pk', 'title']
    inlines = [ProductImages, ProductSpecifications]
    list_filter = ['active', 'limited_edition', 'freeDelivery', 'rating']
    search_fields = ['title', 'category', 'price']
    actions = ['make_active', 'make_inactive']
    fieldsets = (
        ('О продукте', {
            'fields': ('category', 'title', ('price', 'count', 'rating'))
        }),
        ('Дополнительные параметры', {
            'classes': ('collapse',),
            'fields': ('limited_edition', 'freeDelivery', 'active')
        }),
        ('Описание товара', {
            'classes': ('collapse',),
            'fields': ('fullDescription',),
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent__gte=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @admin.action(description='Сделать активным')
    def make_active(self, request, product):
        updated = product.update(active=True)
        self.message_user(request, message=f'Активные продукты: {updated}')

    @admin.action(description='Сделать неактивным')
    def make_inactive(self, request, product):
        updated = product.update(active=False)
        self.message_user(request, message=f'Неактивные продукты: {updated}')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product', 'price', 'salePrice']
    list_display_links = ['pk', 'product']
