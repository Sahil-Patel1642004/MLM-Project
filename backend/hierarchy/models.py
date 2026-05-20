from django.db import models

from backend.employees.models import Employees

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.role_name


class Hierarchy(models.Model):



    POSITION_CHOICES = (
        ('left', 'Left'),
        ('right', 'Right'),
    )

    employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE
    )

    parent_employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE,
        related_name='child_employees'
    )

    level = models.IntegerField(default=1)

    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES
    )

    total_left = models.IntegerField(default=0)

    total_right = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.employee_id