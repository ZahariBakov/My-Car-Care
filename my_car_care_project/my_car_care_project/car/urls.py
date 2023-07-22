from django.urls import path, include

from my_car_care_project.car.views import CarPageView, CarAddView, CarDetailsView, car_edit_view, CarDeleteView

urlpatterns = (
    path('', CarPageView.as_view(), name='car page'),
    path('add/', CarAddView.as_view(), name='car add'),
    path('<int:car_id>/', include([
        path('', CarDetailsView.as_view(), name='car details'),
        path('edit/', car_edit_view, name='car edit'),
        path('delete/', CarDeleteView.as_view(), name='car delete'),
    ])),
)
