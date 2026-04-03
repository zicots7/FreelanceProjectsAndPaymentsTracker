from django.db import models
from django.utils import timezone

class Payment(models.Model):
    milestone = models.ForeignKey(
        'Milestone.Milestone',
        on_delete=models.CASCADE,
        null=False,
        related_name="payments"
        )
    amount_paid = models.BigIntegerField(null=False)
    date_paid = models.DateField(default=timezone.now)
    methods = [("UPI","UPI"),
               ("CARD","CARD"),
               ("CASH","CASH"),
               ("NET BANKING","NET BANKING"),
               ("CRYPTO","CRYPTO"),
               ]
    payment_method = models.CharField(choices=methods,null=False,max_length=100)
    def __str__(self):
        return f"{self.id}-{self.milestone} - {self.amount_paid}"
    class Meta:
        db_table = "payment"

"""
Payment table:
Pid = primary key with unique and auto increment constrain.
milestone = foreginKey from Milestone Table with CASCADE on delete and not null constrain.
amount_paid = project amount paid by client with notnull constrain.
date_paid = payment data when payment is made.
methods= contains options of (UPI, CARD,CASH,NET BANKING,CRYPTO).
payment_method = has multiple choices of payment method from methods, with notnull constrain.

"""