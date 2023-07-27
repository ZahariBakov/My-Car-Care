from django.urls import path
from my_car_care_project.common.views import IndexView, learn_more_view

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('learn_more/', learn_more_view, name='learn more'),
)
