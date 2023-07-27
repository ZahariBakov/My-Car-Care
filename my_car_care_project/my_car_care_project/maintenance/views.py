from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from my_car_care_project.car.models import Car
from my_car_care_project.maintenance.forms import MaintenanceAddForm, MaintenanceEditForm, RepairEditForm
from my_car_care_project.maintenance.models import Maintenance, Repair


def is_maintenance_group_user(user):
    return user.is_superuser or user.groups.filter(name='master_user').exists() or user.groups.filter(
        name='maintenance_moderator').exists()


def is_car_group_user(user):
    return user.is_superuser or user.groups.filter(name='master_user').exists() or user.groups.filter(
        name='car_moderator').exists()


@user_passes_test(is_maintenance_group_user)
def maintenance_page(request):
    maintenances = Maintenance.objects.all()
    repairs = Repair.objects.all()

    context = {
        'maintenances': maintenances,
        'repairs': repairs,
    }
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

    context = {
        'maintenance': maintenance,
        'form': form,
        'car': car,
    }

    return render(request, 'maintenance/maintenance-edit-page.html', context)


class MaintenanceDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'maintenance/maintenance-delete-page.html'
    model = Maintenance
    extra_context = {'title': 'Are you sure you want to delete this maintenance?'}
    success_url = reverse_lazy('maintenance')

    def get_object(self, queryset=None):
        maintenance_id = self.kwargs.get('maintenance_id')
        return get_object_or_404(Maintenance, pk=maintenance_id)


@user_passes_test(is_car_group_user)
def repair_edit_view(request, repair_id):
    repair = get_object_or_404(Repair, pk=repair_id)

    if request.method == 'POST':
        form = RepairEditForm(request.POST, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('maintenance')
    else:
        form = RepairEditForm(instance=repair)  # Use 'instance=repair' to populate the form with data

    context = {
        'form': form,
        'repair': repair,
    }

    return render(request, 'History/history-edit-page.html', context)

