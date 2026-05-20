from django.db import models

from backend.employees.models import Employees


# Create your models here.
class Wallet(models.Model):

    employee = models.OneToOneField(
        Employees,
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


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    TRANSACTION_CATEGORIES = [
        ('salary', 'Salary'),
        ('commission', 'Commission'),
        ('bonus', 'Bonus'),
        ('withdrawal', 'Withdrawal'),
        ('transfer', 'Transfer'),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)

    category = models.CharField(max_length=20, choices=TRANSACTION_CATEGORIES)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} ({self.wallet.employee})"

