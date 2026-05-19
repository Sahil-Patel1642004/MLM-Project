from django.db import models

# Create your models here.
class ySalar(models.Model):

    INCREMENT_TYPE = (
        ('monthly', 'Monthly'),
        ('promotion', 'Promotion'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    old_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    increment_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    increment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    new_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    increment_type = models.CharField(
        max_length=50,
        choices=INCREMENT_TYPE
    )

    approved_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name='salary_approved_by'
    )

    effective_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.employee_id