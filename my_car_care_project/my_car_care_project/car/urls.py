from django.urls import path

from my_car_care_project.car.views import CarPageView, CarAddView, CarDetailsView

urlpatterns = (
    path('', CarPageView.as_view(), name='car page'),
    path('add/', CarAddView.as_view(), name='car add'),
    path('<int:car_id>/', CarDetailsView.as_view(), name='car details'),
)
