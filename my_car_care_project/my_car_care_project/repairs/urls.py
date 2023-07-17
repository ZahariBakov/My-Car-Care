from django.urls import path

from my_car_care_project.repairs.views import repairs_page

urlpatterns = (
    path('', repairs_page, name='repairs'),
)
