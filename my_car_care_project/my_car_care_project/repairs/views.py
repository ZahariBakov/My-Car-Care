from django.shortcuts import render
from my_car_care_project.repairs.models import Repair


def repairs_page(request):
    repairs = Repair.objects.all()
    context = {'repairs': repairs}
    return render(request, 'repairs/repairs-page.html', context)
