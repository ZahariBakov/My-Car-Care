from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from my_car_care_project.accounts.models import Profile

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    fields = '__all__'


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'profile_picture')
