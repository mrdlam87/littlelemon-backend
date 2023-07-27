from django.contrib import admin

# Register your models here.
from .models import MenuItem, Booking, Category

admin.site.register(MenuItem)
admin.site.register(Booking)
admin.site.register(Category)
