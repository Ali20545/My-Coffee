from django.contrib import admin
from .models import Coffees
from django.utils.html import format_html
# Register your models here.

class Coffeeadmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'Product_Name', 'Description', 'create_date')
    list_display_links = ('id', 'thumbnail', 'Product_Name',)
    search_fields = ('Product_Name', 'Description',)
    list_filter = ('Product_Name','Description',)
    


admin.site.register(Coffee, Coffeeadmin)