from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "SwiftNest"
admin.site.site_title = "Ecomm Shopping Site Made by AbdulHaie"
admin.site.index_title = "Manage your shoping Abdul Haie"

admin.site.register(Products)
admin.site.register(Order)
