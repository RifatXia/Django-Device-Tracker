from django.db import models
from django.conf import settings

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

    def __str__(self):
        return self.name
    
# the log to keep track of the devices borrowed by the employees
# along with keeping track of the condition of the device when it is borrowed and returned
class DeviceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    device = models.ForeignKey(settings.DEVICE_MODEL, on_delete=models.CASCADE, null=True)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    # this fields are to keep track of the condition of the device on checkout and return 
    # one way to implement this would be to link django forms to the frontend file 
    # us a text-box for taking the input of the condition during the checkout and return accordinly 
    condition_on_checkout = models.CharField(max_length=1000, blank=True)
    condition_on_return = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.employee.name + " - " + self.device.brand
