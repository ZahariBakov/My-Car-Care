from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from my_car_care_project.accounts.models import Profile

UserModel = get_user_model()


class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

        self.master_user_group = Group.objects.create(name='master_user')
        self.car_moderator_group = Group.objects.create(name='car_moderator')
        self.maintenance_moderator_group = Group.objects.create(name='maintenance_moderator')

    def test_register_view(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('register user'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserModel.objects.count(), 1)

    def test_login_view(self):
        response = self.client.get(reverse('login user'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login user'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_profile_details_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile details', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
