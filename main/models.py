from tabnanny import verbose
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        if not self.slug:
            # Транслитерация перед созданием slug
            self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', verbose_name="Изображение")

    def __str__(self):
        return f"Image for {self.product.name}"



class Advantage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.CharField(max_length=2047, verbose_name='Текст')
    emoji = models.CharField(max_length=8, verbose_name='Эмоджи')

    def __str__(self):
        return f"{self.title}"
