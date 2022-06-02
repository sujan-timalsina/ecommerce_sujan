from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Brand)
admin.site.register(Category)
# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
