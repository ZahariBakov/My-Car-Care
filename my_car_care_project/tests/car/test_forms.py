from django.contrib.auth import get_user_model
from django.test import TestCase
from my_car_care_project.car.forms import CarAddForm, CarEditForm
from my_car_care_project.car.models import Car

UserModel = get_user_model()


class CarFormsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_car_add_form_valid_data(self):
        form = CarAddForm(data={
            'brand': 'Toyota',
            'model': 'Camry',
            'year': 2023,
        })
        self.assertTrue(form.is_valid())

    def test_car_add_form_invalid_data(self):
        form = CarAddForm(data={})
        self.assertFalse(form.is_valid())

    def test_car_edit_form_valid_data(self):
        car = Car.objects.create(
            brand='Toyota',
            model='Camry',
            year=2023,
            user=self.user
        )
        form = CarEditForm(instance=car, data={
            'brand': 'Toyota',
            'model': 'Camry',
            'year': 2023,
            'odometer': 10000,
            'purchase_price': 25000.00,
            'date_of_purchase': '2023-01-01',
        })
        self.assertTrue(form.is_valid())

    def test_car_edit_form_invalid_data(self):
        form = CarEditForm(data={})
        self.assertFalse(form.is_valid())
