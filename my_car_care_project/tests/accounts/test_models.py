from django.test import TestCase
from my_car_care_project.accounts.models import Profile


class ProfileModelTest(TestCase):
    def test_full_name(self):
        # Create a profile with a first name and last name
        profile = Profile(first_name='John', last_name='Doe')
        self.assertEqual(profile.full_name, 'John Doe')

        # Create a profile with only a first name
        profile = Profile(first_name='Alice')
        self.assertEqual(profile.full_name, 'Alice ')

        # Create a profile with only a last name
        profile = Profile(last_name='Smith')
        self.assertEqual(profile.full_name, ' Smith')

        # Create a profile with no first name or last name
        profile = Profile()
        self.assertIsNone(profile.full_name)

    def test_email_unique(self):
        # Test that the email field is unique
        profile1 = Profile.objects.create(email='test@example.com')

        # Attempt to create another profile with the same email
        with self.assertRaises(Exception):
            profile2 = Profile(email='test@example.com')
            profile2.save()
