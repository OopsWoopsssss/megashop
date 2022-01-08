from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Product, ProductShots, Review, Rating, RatingStar


class ReviewInline(admin.TabularInline):
    """Отзывы на странице продукта"""
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ProductShotsInLine(admin.TabularInline):
    model = ProductShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Изображение'


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Товары"""

    inlines = [ProductShotsInLine, ReviewInline]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_image',)
    form = ProductAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="100"')

    get_image.short_description = 'Постер'


@admin.register(ProductShots)
class ProductShotsAdmin(admin.ModelAdmin):
    """Снимки товара"""
    list_display = ('product', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Изображение'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к продукту"""
    list_display = ("name", "email", "parent", "product", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "product", "ip")


admin.site.register(RatingStar)

admin.site.site_title = 'Админка MEGA SHOP'
admin.site.site_header = 'Админка MEGA SHOP'
