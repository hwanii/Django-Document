from django.contrib import admin


from .models import Manufacturer, Car, Person, Pokemon, Type

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Person)
admin.site.register(Pokemon)
admin.site.register(Type)
