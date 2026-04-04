from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    ROLE_CHOICES = [
        ('admin','admin'),
        ('client','client'),
    ]
    role = models.CharField(choices=ROLE_CHOICES,max_length=20,default='client',null=False)
    is_demo = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.username} ({self.role})"
    def is_admin(self):
        return self.role == "admin"
    def is_client(self):
        return self.role == "client"
    class Meta:
        db_table = "customer"