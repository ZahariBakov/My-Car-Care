from django import forms

from my_car_care_project.maintenance.models import Maintenance


class MaintenanceAddForm(forms.ModelForm):
    # date = forms.DateField(input_formats=['dd.dm.YY'])
    date = forms.DateField(input_formats=['%d.%m.%y'])

    class Meta:
        model = Maintenance
        fields = ['title', 'description', 'date', 'cost', 'status']