from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic as views
from my_car_care_project.car.forms import CarAddForm
from my_car_care_project.car.models import Car


class CarPageView(LoginRequiredMixin, views.TemplateView):
    template_name = 'car/car-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = self.request.user.car_set.all()
        return context


class CarAddView(views.CreateView):
    template_name = 'car/car-add-page.html'
    form_class = CarAddForm

    def get_success_url(self):
        return reverse('car page', kwargs={
            'pk': self.object.pk
        })

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user

        return form


class CarDetailsView(views.DetailView):
    template_name = 'car/car-details-page.html'
    model = Car

    def get_object(self, queryset=None):
        car_id = self.kwargs.get('car_id')
        return get_object_or_404(Car, id=car_id)
