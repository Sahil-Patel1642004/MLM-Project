from django.db import models

from backend.employees.models import Employees
from backend.hierarchy.models import Role

# Create your models here.
class Promotion(models.Model):

    employee = models.ForeignKey(
        Employees,

        on_delete=models.CASCADE
    )

    old_role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name='old_roles'
    )

    new_role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name='new_roles'
    )

    old_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    new_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    promotion_reason = models.TextField()

    promoted_by = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True,
        related_name='promoted_by_employee'
    )

    promotion_date = models.DateField()

    def __str__(self):
        return self.employee.employee_id