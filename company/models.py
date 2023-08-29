from django.db import models

class Company(models.Model):
    name = models.CharField('Company Name', max_length=100)
    year = models.DateTimeField()

    def get_employee_count(self):
        return self.employee_set.count()

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField('Employee Name', max_length=100)
    position = models.CharField('Employee Position', max_length=100)
    salary = models.DecimalField('Employee Salary')
    joining_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
