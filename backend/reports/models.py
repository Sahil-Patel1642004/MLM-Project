from django.db import models
from backend.employees.models import Employees


class Report(models.Model):

    REPORT_TYPES = [
        ('salary', 'Salary'),
        ('commission', 'Commission'),
        ('attendance', 'Attendance'),
        ('performance', 'Performance'),
        ('wallet', 'Wallet'),
    ]

    employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE,
        related_name='reports'
    )

    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)

    description = models.TextField(blank=True)

    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} - {self.employee}"
