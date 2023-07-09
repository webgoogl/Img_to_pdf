from django.contrib import admin
from api.models import *
# Register your models here.

@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=('name','age')

@admin.register(Book)
class bookadmin(admin.ModelAdmin):
    list_display=('book',)

@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display=('category',)

@admin.register(excel_export)
class excel_exportAdmin(admin.ModelAdmin):
    list_display=('excel',)