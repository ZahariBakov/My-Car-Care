from django.contrib import admin

from my_car_care_project.repairs.models import Repair


@admin.register(Repair)
class RepairModelAdmin(admin.ModelAdmin):
    pass
