from django.urls import path

from my_car_care_project.maintenance.views import maintenance_page, MaintenanceAddView

urlpatterns = (
    path('', maintenance_page, name='maintenance'),
    path('add/<int:car_id>/', MaintenanceAddView.as_view(), name='maintenance_add'),
)
