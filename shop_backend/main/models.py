from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категгории"""
    name = models.CharField('Категория', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """ Товар """
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='product/')
    price = models.DecimalField('Цена', default=0, decimal_places=2, max_digits=1000)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class ProductShots(models.Model):
    """Снимки товара"""
    image = models.ImageField('Снимки', upload_to='product_shots/')
    product = models.ForeignKey(Product, verbose_name='Продукты', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Снимки товара'
        verbose_name_plural = 'Снимки товара'