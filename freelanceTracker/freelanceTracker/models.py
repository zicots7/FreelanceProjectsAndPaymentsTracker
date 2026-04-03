from django.db import models

class Account (models.Model):
    roles = models.TextChoices("admin","")