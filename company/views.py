from django.shortcuts import render
from .models import DeviceLog, Employee
from device.models import Device

# the api endpoint to checkout a device 
def device_checkout(employee_id, device_id):
    device = Device.objects.get(pk=device_id)

    if device.is_borrowed:
        pass
    else:
        # if the device is not borrowed, pairing up the employee and the device
        # then marking the device as borrowed
        employee = Employee.objects.get(pk=employee_id)
        device_log = DeviceLog.create(employee=employee, device=device)
        device_log.save()

        device.is_borrowed = True
        device.save()