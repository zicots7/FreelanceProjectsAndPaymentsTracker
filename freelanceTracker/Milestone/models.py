
from django.db import models

# Create your models here.
class Milestone (models.Model):

    project_name = models.ForeignKey(
        'Project.Project',
        on_delete=models.CASCADE,
        null=False,
        related_name='milestones',
    )
    description = models.CharField(max_length=500,null=False)
    amount = models.BigIntegerField(null=False)
    due_date = models.DateField(null=False)
    paid_status = [("Yes","Yes"),
                   ("No","No"),]
    is_paid = models.CharField(choices=paid_status,max_length=50,null=False)
    def __str__(self):
        return self.description
    class Meta:
        db_table = "milestone"
"""
Milestone class's Attributes 
id = automatically generated my django with primaryLey constrain.
project_name = ForeginKey using Project with cascade on delete operation,
with related_name which will later be use to call milestone.project.all().
description = description about Milestone , not null constrain .
amount = project amount , not null constrain .
due_date = amount due date for projects , not null constrain .
paid_status = having option (Yes/No).
is_paid = shows the status of project payment, not null constrain .
"""
