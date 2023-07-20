from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Car(models.Model):
    brand = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField()

    odometer = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    purchase_price = models.FloatField(
        blank=True,
        null=True
    )

    date_of_purchase = models.DateField(
        blank=True,
        null=True
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='vehicle'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.brand} {self.model}"
