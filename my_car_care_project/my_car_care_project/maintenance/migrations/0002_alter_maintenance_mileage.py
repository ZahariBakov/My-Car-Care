# Generated by Django 4.2.2 on 2023-07-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='mileage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
