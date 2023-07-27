from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter
def user_can_see_maintenance_button(user):
    return user.is_superuser or Group.objects.get(name='master_user').user_set.filter(id=user.id).exists() \
        or Group.objects.get(name='maintenance_moderator').user_set.filter(id=user.id).exists()


@register.filter
def user_can_see_car_button(user):
    return user.is_superuser or Group.objects.get(name='master_user').user_set.filter(id=user.id).exists() \
        or Group.objects.get(name='car_moderator').user_set.filter(id=user.id).exists()
