from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_view, login, get_user_model
from my_car_care_project.accounts.forms import RegisterUserForm, ProfileEditForm
from my_car_care_project.accounts.models import Profile

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


class LogoutUserView(LoginRequiredMixin, auth_view.LogoutView):
    pass


class ProfileDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    profile_image = static('images/person_img.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_image()
        context['cars'] = self.request.user.car_set.all()

        return context


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = Profile
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile details')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, pk=self.kwargs['pk'])

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = Profile
    extra_context = {'title': 'Are you sure you want to delete this profile?'}
    success_url = reverse_lazy('index')
