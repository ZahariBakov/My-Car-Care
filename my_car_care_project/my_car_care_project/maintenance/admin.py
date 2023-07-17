from django.contrib import admin

from my_car_care_project.maintenance.models import Maintenance


@admin.register(Maintenance)
class MaintenanceModelAdmin(admin.ModelAdmin):
    pass
