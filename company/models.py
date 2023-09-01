from django.db import models
from device.models import Device

class Company(models.Model):
    name = models.CharField('Company Name', max_length=100)
    year = models.DateTimeField()

    def get_employee_count(self):
        return self.employee_set.count()
    
    def __str__(self):
        return self.name

# Employee shares a "is a" relationship with the Company and hence the use of the company as a foreign key 
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField('Employee Name', max_length=100)
    position = models.CharField('Employee Position', max_length=100)
    salary = models.DecimalField('Employee Salary', decimal_places=2, max_digits=20)
    joining_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return self.name
