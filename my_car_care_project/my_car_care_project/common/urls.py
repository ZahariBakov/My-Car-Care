from django.urls import path
from my_car_care_project.common.views import IndexView, learn_more_view, about_us_view

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('learn_more/', learn_more_view, name='learn more'),
    path('about/', about_us_view, name='about us'),
)
