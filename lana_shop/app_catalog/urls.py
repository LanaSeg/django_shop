from django.urls import path
from app_catalog.views import CatalogView, CategoryView, BannersView, TagsView

urlpatterns = [
    path("api/catalog/", CatalogView.as_view()),
    path("api/categories/", CategoryView.as_view()),
    path("api/banners/", BannersView.as_view()),
    path("api/tags/", TagsView.as_view()),
]
