import json

from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from my_car_care_project.car.forms import CarAddForm
from my_car_care_project.car.models import Car


class CarPageView(views.TemplateView):
    template_name = 'car/car-page.html'


class CarAddView(views.CreateView):
    template_name = 'car/car-add-page.html'
    form_class = CarAddForm
    success_url = reverse_lazy('car page')
