from django.contrib import admin
from .models import People, Product, Address, Doctor, Bio
# Register your models here.

admin.site.register(People)

admin.site.register(Product)

admin.site.register(Address)

admin.site.register(Doctor)

admin.site.register(Bio)