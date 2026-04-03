from django.shortcuts import render,redirect,get_object_or_404
from accounts.decorators import admin_required
from .models import Project
from .form import ProjectForm
from Milestone.models import Milestone
from Payment.models import Payment
from Logs.mongoDB import collection
@admin_required
def projectList(request):
    """
    this methods going to return all the listed projects
    :param request: request
    :return: all the projetcs from database
    """
    projects = Project.objects.all()
    return render(request,'projectList.html',{'projects':projects})
@admin_required
def addProject(request):
    """
    :param request: request
    :return: a form to frontend page, so admin can add new projects
    """
    if request.method == "POST":
        projectForm = ProjectForm(request.POST)
        if projectForm.is_valid():
            project = Project.objects.create(
                title = projectForm.cleaned_data['title'],
                client = projectForm.cleaned_data['client'],
                description = projectForm.cleaned_data['description'],
                start_date = projectForm.cleaned_data['start_date'],
                deadline = projectForm.cleaned_data['deadline'],
                status = projectForm.cleaned_data['status'],
                total_value = projectForm.cleaned_data['total_value']
            )
            project.save()
            return redirect('project-add')
    else:
        projectForm = ProjectForm()
    return render(request,'addProject.html',{'projectForm':projectForm})

@admin_required
def deleteProject(request,id):
    """
    :param request:  request
    :param id: take id as for Pid (project ID)
    :return: return project list after deletion successful else return delete project form
    """
    projects = Project.objects.get(Pid=id)
    if request.method == "POST":
        projects = Project.objects.get(Pid=id)
        projects.delete()
        return redirect('project-list')
    return render(request,'deleteProject.html',{'projects':projects})


@admin_required
def updateProject(request,id):
    """

    :param request: POST
    :param id: take project id to perform updation on project
    :return: return updated project details
    """
    projects = Project.objects.get(Pid=id)
    if request.method == "POST":
        projectForm = ProjectForm(request.POST,instance=projects)
        if projectForm.is_valid():
            projectForm.save()
        return redirect('project-list')
    else:
        projectForm = ProjectForm(instance=projects)
    return render(request,'updateProject.html',{'projectForm':projectForm,'projects':projects})

@admin_required
def projectDetails(request,id):
    """

    :param request: POST
    :param id: take particular project id to show details about that project
    :return: return project details page,milestone,payments ,pending amount and total paid
    """
    logs = collection.find({"project_id":id})
    projects = get_object_or_404(
        Project.objects.select_related('client'),Pid=id
    )
    milestone = Milestone.objects.filter(project_name=projects).order_by('due_date')
    payments = Payment.objects.filter(
        milestone__in=milestone
    ).select_related('milestone')
    total_paid = sum(p.amount_paid for p in payments)
    pending = projects.total_value - total_paid
    contexts = {
    "projects":projects,
        "milestones": milestone,
        "payments": payments,
        "total_paid":total_paid,
        "pending":pending,
        "logs":logs,
    }
    return render(request,'projectDetails.html',contexts)