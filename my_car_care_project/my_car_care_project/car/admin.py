from django.contrib import admin
from django.contrib.auth import get_user_model

from my_car_care_project.car.models import Car

UserModel = get_user_model()


@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    pass
