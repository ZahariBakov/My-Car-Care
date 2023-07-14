from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_view, login, get_user_model
from my_car_care_project.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_view.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = static('images/person_img.png')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        context['profile_image'] = profile_image

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete.html'
