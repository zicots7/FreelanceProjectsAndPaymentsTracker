from django.db import models
from django.utils import timezone
from django.conf import settings

class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="client_profile",
    )
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100,null=False)
    platform_choice = [("Fiverr","Fiverr"),
                       ("Upwork","Upwork"),
                       ("Direct","Direct"),
                       ]
    platform = models.CharField(choices=platform_choice,max_length=50,null=False)
    company = models.CharField(max_length=100,blank=True)
    added_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
       return self.first_name + self.last_name
    class Meta:
        db_table = "client"

"""
Made a table called Client , it contains client's necessary details.
name  is client's Name.
email is Client's Email Address.
platform is freelancing platform it can be Fiverr/Upwork/Direct.
date contains exact time and date related to the client project.
"""