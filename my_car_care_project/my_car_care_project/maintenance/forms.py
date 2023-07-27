from django import forms

from my_car_care_project.maintenance.models import Maintenance, Repair


class MaintenanceAddForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d.%m.%y'])

    class Meta:
        model = Maintenance
        fields = ['title', 'description', 'date', 'cost', 'status']


class MaintenanceEditForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'


class RepairEditForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = '__all__'
