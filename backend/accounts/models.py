from django.db import models

# Create your models here.
class Accounts(models.Model):

    role_name = models.CharField(max_length=100)
    role_level = models.IntegerField()

    parent_role = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    basic_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    increment_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    bonus_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    commission_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    max_downline = models.IntegerField(default=0)

    target_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    promotion_after_month = models.IntegerField(default=0)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role_name
