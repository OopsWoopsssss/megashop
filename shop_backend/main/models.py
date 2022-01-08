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
    category = models.ManyToManyField(Category, verbose_name='Категория', related_name='products_categories')
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
    product = models.ForeignKey(Product, verbose_name='Продукты', on_delete=models.CASCADE, related_name='shots')

    class Meta:
        verbose_name = 'Снимки товара'
        verbose_name_plural = 'Снимки товара'


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='children'
    )
    product = models.ForeignKey(Product, verbose_name="продукт", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт", related_name='ratings')

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
