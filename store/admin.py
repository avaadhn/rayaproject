from django.contrib import admin
from django.http.request import HttpRequest
from store.models import Product, Category, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "get_price", "special"]
    list_filter = ["special"]

    def get_price(self, obj):
        return f"{obj.price} تومان"
    
    get_price.short_description = "قیمت محصول"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request):
    #     return False