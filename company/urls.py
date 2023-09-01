from django.urls import path
from . import views

urlpatterns = [
    path('device_checkout/<int:employee_id>/<int:device_id>/', views.device_checkout, name='device_checkout'),
    path('device_return/<int:employee_id>/<int:device_id>/', views.device_return, name='device_return'),
]