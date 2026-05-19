from django.db import models

# Create your models here.
class Employee(models.Model):

    employee_id = models.CharField(
        max_length=50,
        unique=True
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    password = models.CharField(max_length=255)

    profile_image = models.ImageField(
        upload_to='employees/',
        null=True,
        blank=True
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True
    )

    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_employees'
    )

    sponsor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sponsored_employees'
    )

    joining_date = models.DateField()

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    wallet_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_income = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_team = models.IntegerField(default=0)

    total_business = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"