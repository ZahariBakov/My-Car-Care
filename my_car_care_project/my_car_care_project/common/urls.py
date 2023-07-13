from django.urls import path

from my_car_care_project.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
