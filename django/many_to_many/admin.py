from django.contrib import admin

from many_to_many.models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)