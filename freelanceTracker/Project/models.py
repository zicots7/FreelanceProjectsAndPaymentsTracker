from django.db import models


class Project(models.Model):

    Pid = models.BigAutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=100,null=False)
    client = models.ForeignKey(
        'Client.Client',
        on_delete=models.CASCADE,
        null=False,
        related_name="projects"
    )
    description = models.CharField(max_length=300,null=False)
    start_date = models.DateField(null=False)
    deadline = models.DateField(null=False)
    status_choices = [("Complete","Complete"),
                        ("Pending",'Pending'),
                      ("Delivered","Delivered"),]
    status = models.CharField(max_length=100,choices=status_choices,null=False)
    total_value = models.BigIntegerField(null=False)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "project"
"""
Project Table :
Pid = Project id with primarykey constrain.
client = foreginkey from table Client with cascade on delete constrain and  related_name = projects , so later it can
be used to call them [client.projects.all()]
description = details about the project.
start_date = project start date with not null constrain.
deadline = project deadline with no null constrain.
status_choices = having multiple choices like (complete , pending , not started yet , delivered).
status = shows status of the project having choices as choice.
total_value =  total cost of the project.
"""