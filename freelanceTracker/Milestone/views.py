from django.shortcuts import render,redirect,get_object_or_404
from accounts.decorators import admin_required
from .form import MilestoneForm
from.models import Milestone
from Project.models import Project
@admin_required
def addMilestone(request,id):
    """

    :param request: accepts POST request
    :param id: takes milestone id
    :return: returns milestone form and project id
    """
    projects = get_object_or_404(Project.objects.select_related('client'),Pid=id)
    if request.method == "POST":
        milestoneForm = MilestoneForm(request.POST)
        if milestoneForm.is_valid():
            milestone = milestoneForm.save(commit=False)
            milestone.project_name = projects
            milestone.save()
            return redirect('project-details',id=projects.Pid)
    else:
        milestoneForm=MilestoneForm()
    contexts = {'milestoneForm':milestoneForm,
                    'projects':projects
                    }
    return render(request,'addMilestone.html',contexts)

@admin_required
def updateMilestone(request,id):
    """

    :param request: POST request
    :param id: milestone id to perform updation
    :return: return updated milestone details
    """
    milestone = Milestone.objects.get(id=id)
    projects = milestone.project_name
    if request.method =="POST":
        milestoneForm = MilestoneForm(request.POST,instance=milestone)
        if milestoneForm.is_valid():
            milestoneForm.save()
            return redirect('project-details',id=projects.Pid)
    else:
        milestoneForm = MilestoneForm(instance=milestone)
        contexts = {
            "milestone": milestone,
            "projects": projects,
            "milestoneForm":milestoneForm
        }
    return render(request,'updateMilestone.html',contexts)
@admin_required
def deleteMilestone(request,id):
    """

    :param request: POST
    :param id: take project id as input to perform deletion
    :return: return remaining milestone list
    """
    milestone = Milestone.objects.get(id=id)
    projects = milestone.project_name
    if request.method == "POST":
        milestone = Milestone.objects.get(id=id)
        milestone.delete()
        return redirect('project-details',id=projects.Pid)
    else:
        contexts={
            "milestone": milestone,
            "projects":projects
        }
    return render(request,'deleteMilestone.html',contexts)