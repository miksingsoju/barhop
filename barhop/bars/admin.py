from django.contrib import admin
from .models import Bar, Amenity

class BarAdmin(admin.ModelAdmin):
    model = Bar
    list_display = ('bar_name', 'bar_description')

class AmenityAdmin(admin.ModelAdmin):
    model = Amenity
    list_display = ('name',)
# Register your models here.

admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Bar, BarAdmin)