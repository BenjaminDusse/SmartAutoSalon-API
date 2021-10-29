from django.contrib import admin
from .models import CarModel, User, Order

admin.site.register(CarModel)
admin.site.register(User)
admin.site.register(Order)

