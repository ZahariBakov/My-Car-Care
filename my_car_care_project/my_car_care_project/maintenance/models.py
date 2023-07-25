from django.db import models
from my_car_care_project.car.models import Car


class Maintenance(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    date = models.DateField()

    mileage = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.title


class Repair(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='repairs'
    )

    date = models.DateField()

    description = models.TextField()

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Repair on {self.car} - {self.date}"
