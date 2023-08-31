from django.db import models
from company.models import Company

# the base class of all the types of devices, here it is done so that the base class remains the same 
# but the child class can be any type of devices such as laptops, mobiles, etc
# this ensures future extension and addition of more different types of devices
# which would just be the child class of Device
class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # done to ensure so that the device base class doesn't have any table in admin 
    class Meta:
        abstract = True

class Laptop(Device):
    brand = models.CharField()
    added_at = models.DateTimeField(auto_now_add=True)

class Mobile(Device):
    brand = models.CharField()
    added_at = models.DateTimeField(auto_now_add=True)
