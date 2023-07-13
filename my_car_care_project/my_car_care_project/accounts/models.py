from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from my_car_care_project.accounts.validators import validate_only_alphabetical


class Profile(auth_models.AbstractUser):
    USERNAME_MAX_LEN = 20
    USERNAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_alphabetical,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_alphabetical,
        )
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
