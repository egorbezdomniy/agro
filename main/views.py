from django.shortcuts import render, get_object_or_404
from .models import Product, Advantage


# Create your views here.

def index(request):
    advantages = Advantage.objects.all()
    return render(request, 'index.html', context={
        'advantages': advantages
    })

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # Получаем продукт по slug
    images = product.images.all()  # Получаем все изображения, связанные с продуктом
    return render(request, 'product_detail.html', {'product': product, 'images': images})
