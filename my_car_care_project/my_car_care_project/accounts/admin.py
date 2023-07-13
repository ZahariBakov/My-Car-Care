from django.contrib import admin
from django.contrib.auth import get_user_model

from my_car_care_project.accounts.models import Profile

UserModel = get_user_model()


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    pass
