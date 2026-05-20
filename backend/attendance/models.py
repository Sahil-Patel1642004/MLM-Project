from django.db import models

from backend.employees.models import Employees

# Create your models here.
class Attendance(models.Model):


    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )

    employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE
    )



    check_in = models.DateTimeField()

    check_out = models.DateTimeField(
        null=True,
        blank=True
    )

    total_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.employee_id