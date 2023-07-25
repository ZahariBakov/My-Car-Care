from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_car_care_project.common.urls')),
    path('car/', include('my_car_care_project.car.urls')),
    path('accounts/', include('my_car_care_project.accounts.urls')),
    path('maintenance/', include('my_car_care_project.maintenance.urls')),
]
