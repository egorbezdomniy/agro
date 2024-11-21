from django.urls import path

from main import views

urlpatterns = [
    path('catalog', views.catalog, name='catalog'),
    path('', views.index, name='index'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
]