from django.db import models

# Create your models here.
class Commissions(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )

    from_employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='commission_from'
    )

    to_employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='commission_to'
    )

    level_no = models.IntegerField()

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True
    )

    business_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    commission_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    commission_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.to_employee.employee_id