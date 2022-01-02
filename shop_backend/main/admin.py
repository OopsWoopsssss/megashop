from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, ProductShots


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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Товары"""
    list_display = ('title', 'category', 'url')
    search_fields = ('title', 'category__name')
    inlines = [ProductShotsInLine]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_image',)

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


admin.site.site_title = 'Админка MEGA SHOP'
admin.site.site_header = 'Админка MEGA SHOP'
