from django.contrib import admin

from my_car_care_project.maintenance.models import Maintenance, Repair


@admin.register(Maintenance)
class MaintenanceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Repair)
class RepairModelAdmin(admin.ModelAdmin):
    pass
