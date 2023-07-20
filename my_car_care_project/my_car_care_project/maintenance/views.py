from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic as views

from my_car_care_project.car.models import Car
from my_car_care_project.maintenance.forms import MaintenanceAddForm
from my_car_care_project.maintenance.models import Maintenance


def maintenance_page(request):
    maintenance = Maintenance.objects.all()
    context = {'maintenance': maintenance}
    return render(request, 'maintenance/maintenance-page.html', context)


class MaintenanceAddView(views.View):
    template_name = 'maintenance/maintenance-add-page.html'
    form_class = MaintenanceAddForm

    def get(self, request, *args, **kwargs):
        car_id = kwargs['car_id']
        car = get_object_or_404(Car, id=car_id)
        form = self.form_class()
        context = {'form': form, 'car': car}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        car_id = kwargs['car_id']
        car = get_object_or_404(Car, id=car_id)
        form = self.form_class(request.POST)
        print("Form valid:", form.is_valid())
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.car = car
            maintenance.save()
            print("Maintenance saved:", maintenance)
            return HttpResponseRedirect(reverse('car details', kwargs={'car_id': car_id}))
        context = {'form': form, 'car': car}
        return render(request, self.template_name, context)


