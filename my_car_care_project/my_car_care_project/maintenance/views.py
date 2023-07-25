from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic as views

from my_car_care_project.car.models import Car
from my_car_care_project.maintenance.forms import MaintenanceAddForm, MaintenanceEditForm
from my_car_care_project.maintenance.models import Maintenance, Repair


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

        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.car = car
            maintenance.save()
            print("Maintenance saved:", maintenance)
            return HttpResponseRedirect(reverse('car details', kwargs={'car_id': car_id}))
        context = {'form': form, 'car': car}
        return render(request, self.template_name, context)


def maintenance_edit_view(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
    car = maintenance.car

    if request.method == 'POST':
        form = MaintenanceEditForm(request.POST, instance=maintenance)

        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.car = car
            maintenance.save()

            if 'add_to_history' in request.POST:
                repair = Repair.objects.create(
                    car=car,
                    date=maintenance.date,
                    description=maintenance.description,
                    cost=maintenance.cost,
                )

                maintenance.delete()
                return redirect('car details', car_id=car.pk)

            return redirect('car details', car_id=car.pk)
    else:
        form = MaintenanceEditForm(instance=maintenance)

    maintenances = Maintenance.objects.filter(car=car)

    context = {
        'maintenance': maintenance,
        'form': form,
        'car': car,
        'maintenances': maintenances,
    }

    return render(request, 'maintenance/maintenance-edit-page.html', context)
