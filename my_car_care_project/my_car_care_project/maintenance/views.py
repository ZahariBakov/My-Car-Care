from django.shortcuts import render
from my_car_care_project.maintenance.models import Maintenance


def maintenance_page(request):
    maintenance = Maintenance.objects.all()
    context = {'maintenance': maintenance}
    return render(request, 'maintenance/maintenance-page.html', context)
