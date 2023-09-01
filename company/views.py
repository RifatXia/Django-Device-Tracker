from django.utils import timezone
from django.shortcuts import render
from .models import DeviceLog, Employee
from device.models import Device
from django.core.exceptions import ObjectDoesNotExist

# the api endpoint to checkout a device 
def device_checkout(request, employee_id, device_id):
    device = Device.objects.get(pk=device_id)

    # if the device would already be borrowed, it cannot be further allocated to an employee
    # if the device is not borrowed, pairing up the employee and the device
    # then marking the device as borrowed
    if device.is_borrowed == False:
        employee = Employee.objects.get(pk=employee_id)
        device_log = DeviceLog.objects.create(
            employee=employee, 
            device=device,
        )
        device_log.save()

        device.is_borrowed = True
        device.save()

        # render accordingly
        # return render('')

# the api endpoint to return a device
def device_return(request, employee_id, device_id):
    # getting the device log of the employee with the device
    # setting it up in a try catch block to avoid error due to inability to find a device log 
    try:
        device_log = DeviceLog.objects.get(employee_id=employee_id, device_id=device_id)
        device_log.return_date = timezone.now()
        device_log.save()

        # since the device is no longer occupied, is_borrowed is marked as false
        # so that the device can be accessible to the other employees 
        device = device_log.device
        device.is_borrowed = False
        device.save()

        # render accordingly
        # return render('')

    except ObjectDoesNotExist:
        device_log = None