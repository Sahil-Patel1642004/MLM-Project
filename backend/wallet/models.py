from django.db import models

# Create your models here.
class Wallet(models.Model):

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE
    )

    main_wallet = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    commission_wallet = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    bonus_wallet = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    salary_wallet = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    withdraw_wallet = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee.employee_id