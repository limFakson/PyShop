from django.contrib import admin
from .models import Product, Offer, NewProduct



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')



class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
    
class NewProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(NewProduct, NewProductAdmin)