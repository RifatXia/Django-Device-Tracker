from django.urls import path
from . import views

urlpatterns = [
    # the urls work in the following way - the name of the api endpoint/employee_id/device_id/
    # the 'name' field in the url demonstrated that instead of using 'device_checkout', we can also use the name to invoke the views
    # this comes handy during the implementation of the django in the HTML templates for the project
    path('device_checkout/<int:employee_id>/<int:device_id>/', views.device_checkout, name='device_checkout'),
    path('device_return/<int:employee_id>/<int:device_id>/', views.device_return, name='device_return'),
]