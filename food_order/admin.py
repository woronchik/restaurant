from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'is_available')
    actions = ['make_unavailable']

    def make_unavailable(self, request, queryset):
        queryset.update(is_available=False)
        self.message_user(request, "Выбранные продукты были поставлены на стоп")
    make_unavailable.short_description = "Поставить выбранные продукты на стоп"


admin.site.register(Product, ProductAdmin)
