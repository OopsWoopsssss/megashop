from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    """Категгории"""
    name = models.CharField('Категория', max_length=150)

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
    quantity = models.PositiveSmallIntegerField('Количество на складе', default=0)
    sale = models.BooleanField('Акция', default=False)
    discount = models.PositiveSmallIntegerField('Процент скидки', default=0)


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


class Profile(AbstractUser):
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'profile_pic']

    def __str__(self):
        return self.username


class Rating(models.Model):
    """Рейтинг"""
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField(
        "Звезда", validators=[MaxValueValidator(5)], default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт", related_name='ratings')


    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """Отзывы"""
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='children'
    )
    product = models.ForeignKey(Product, verbose_name="продукт", on_delete=models.CASCADE, related_name="reviews")
    create_data = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Cart(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, verbose_name='Тровары', related_name='products')

