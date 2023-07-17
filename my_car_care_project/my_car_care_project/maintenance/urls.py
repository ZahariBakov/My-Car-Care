from django.urls import path

from my_car_care_project.maintenance.views import maintenance_page

urlpatterns = (
    path('', maintenance_page, name='maintenance'),
)
