from django.urls import path, include

from my_car_care_project.car.views import CarPageView, CarAddView

urlpatterns = (
    path('', CarPageView.as_view(), name='car page'),
    path('add/', CarAddView.as_view(), name='car add'),
)
