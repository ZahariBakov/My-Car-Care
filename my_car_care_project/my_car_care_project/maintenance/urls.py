from django.urls import path

from my_car_care_project.maintenance.views import maintenance_page, MaintenanceAddView, maintenance_edit_view, \
    MaintenanceDeleteView, repair_edit_view

urlpatterns = (
    path('', maintenance_page, name='maintenance'),
    path('add/<int:car_id>/', MaintenanceAddView.as_view(), name='maintenance_add'),
    path('edit/<int:maintenance_id>/', maintenance_edit_view, name='maintenance edit'),
    path('delete/<int:maintenance_id>/', MaintenanceDeleteView.as_view(), name='maintenance delete'),
    path('repair/edit/<int:repair_id>/', repair_edit_view, name='history edit'),
)
