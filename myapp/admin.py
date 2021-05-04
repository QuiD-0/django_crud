from django.contrib import admin
from .models import Menu


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'img_path']
    list_display_link = ['name', 'description', 'price', 'img_path']
