from django.db import models

from backend.employees.models import Employees

# Create your models here.
class Performance(models.Model):

    employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE
    )


    month = models.CharField(max_length=20)

    sales_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    target_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    completed_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    bonus_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.employee_id