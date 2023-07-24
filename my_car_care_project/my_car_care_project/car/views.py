from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from my_car_care_project.car.forms import CarAddForm, CarEditForm
from my_car_care_project.car.models import Car
from my_car_care_project.maintenance.models import Maintenance
from my_car_care_project.repairs.models import Repair


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
        return reverse('car details', kwargs={
            'car_id': self.object.pk
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        repairs = Repair.objects.filter(car=car)
        maintenances = Maintenance.objects.filter(car=car)
        context['repairs'] = repairs
        context['maintenances'] = maintenances
        return context


@login_required
def car_edit_view(request, car_id):
    car = Car.objects.filter(pk=car_id).get()
    form = CarEditForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect('car details', car_id=car_id)

    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-edit-page.html', context)


class CarDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'car/car-delete-page.html'
    model = Car
    extra_context = {'title': 'Are you sure you want to delete this car?'}
    success_url = reverse_lazy('car page')

    def get_object(self, queryset=None):
        car_id = self.kwargs.get('car_id')
        return get_object_or_404(Car, pk=car_id)
