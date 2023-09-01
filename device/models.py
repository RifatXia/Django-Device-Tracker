from django.utils import timezone
from django.db import models
# from company.models import Company
from django.conf import settings

# the base class of all the types of devices, here it is done so that the base class remains the same 
# but the child class can be any type of devices such as laptops, mobiles, etc
# this ensures future extension and addition of more different types of devices
# which would just be the child class of Device
class Device(models.Model):
    company = models.ForeignKey(settings.COMPANY_MODEL, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    bought_at = models.DateTimeField(default=timezone.now)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.brand

class Laptop(Device):
    ram = models.IntegerField(default=1)
    rom = models.IntegerField(default=1)

class Mobile(Device):
    camera = models.IntegerField(default=10)