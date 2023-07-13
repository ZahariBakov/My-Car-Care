from django.views import generic as views
from django.contrib.auth import views as auth_view


class RegisterUserView(views.RedirectView):
    pass


class LoginUserView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_view.LogoutView):
    pass
