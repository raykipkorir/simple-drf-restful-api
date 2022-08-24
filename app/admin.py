from django.contrib import admin

from .models import Drink


class DrinkModelAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

admin.site.register(Drink, DrinkModelAdmin)
