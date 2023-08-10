from django import forms

from my_car_care_project.car.models import Car


class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year']


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('user',)
