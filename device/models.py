from django.utils import timezone
from django.db import models
from company.models import Company

# the base class of all the types of devices, here it is done so that the base class remains the same 
# but the child class can be any type of devices such as laptops, mobiles, etc
# this ensures future extension and addition of more different types of devices
# which would just be the child class of Device
class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bought_at = models.DateTimeField(default=timezone.now)

    # done to ensure so that the device base class doesn't have any table in admin 
    class Meta:
        abstract = True

class Laptop(Device):
    brand = models.CharField(max_length=100)
    ram = models.IntegerField(default=1)
    rom = models.IntegerField(default=1)
    
    def __str__(self):
        return self.brand

class Mobile(Device):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand
