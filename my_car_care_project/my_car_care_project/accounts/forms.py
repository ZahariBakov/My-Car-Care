from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    fields = '__all__'


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
