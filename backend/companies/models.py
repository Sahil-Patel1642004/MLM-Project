from django.db import models

# Create your models here.
class Companies(models.Model):

    company_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name