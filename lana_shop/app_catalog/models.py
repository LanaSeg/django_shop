from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ["title", "pk"]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    title = models.CharField(max_length=128, db_index=True, verbose_name='название')
    active = models.BooleanField(default=False, verbose_name='активная')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='subcategories',
                               verbose_name='родитель')
    favourite = models.BooleanField(default=False, verbose_name='избранная категория')

    def href(self):
        return f'/catalog/{self.pk}'

    def __str__(self):
        return self.title


def category_image_directory_path(instance: 'CategoryIcons', filename):  # путь загрузки иконок
    if instance.category.parent:
        return f'app_catalog/icons/{instance.category.parent}/{instance.category}/{filename}'
    else:
        return f'app_catalog/icons/{instance.category}/{filename}'


class CategoryIcons(models.Model):
    class Meta:
        ordering = ["pk"]
        verbose_name = "иконка категории"
        verbose_name_plural = "иконки категорий"

    src = models.FileField(upload_to=category_image_directory_path, max_length=500, verbose_name='иконка')
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='image', verbose_name='категория',
                                    blank=True, null=True)

    def alt(self):
        return self.category.title

    def __str__(self):
        return f'{self.pk} иконка'
