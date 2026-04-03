from django.shortcuts import render,redirect,get_object_or_404
from accounts.decorators import admin_required
from .form import paymentForm
from .models import Payment
from Milestone.models import Milestone
from Project.models import Project
from django.contrib import messages
from io import BytesIO
import openpyxl
@admin_required
def addPayment(request,id):
    """
    :param request: POST request
    :param id: payment ID
    :return: context with project id and renders payment form
    """
    projects = get_object_or_404(Project.objects.select_related('client'),Pid=id)
    if request.method =="POST":
        form = paymentForm(request.POST)
        form.fields['milestone'].queryset = Milestone.objects.filter(project_name=projects)
        if form.is_valid():
            form.save()
            return redirect('project-details',id=projects.Pid)
    else:
        form = paymentForm()
        form.fields['milestone'].queryset = Milestone.objects.filter(project_name=projects)
    contexts= {"form":form,
                   "projects":projects
                   }

    return render(request,'addPayment.html',contexts)
@admin_required
def updatePayment(request,id):
    """

    :param request: POST request
    :param id: project id and payment id
    :return: payment form and payment id ,project id
    """
    payment = Payment.objects.get(id=id)
    projects = payment.milestone.project_name
    if request.method == "POST":
        form = paymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('project-details', id=projects.Pid)
    else:
        form = paymentForm(instance=payment)
        contexts = {
            "payment": payment,
            "projects": projects,
            "form": form
        }
    return render(request,'updatePayment.html',contexts)
@admin_required
def deletePayment(request,id):
    """
    :param request: POST request as parameter
    :param id: takes payment id
    :return: returns id and redirects to project details page otherwise returns contexts with payment id and project id
    """
    payment = Payment.objects.get(id=id)
    projects = payment.milestone.project_name
    if request.method == "POST":
        payment = Payment.objects.get(id=id)
        payment.delete()
        return redirect('project-details', id=projects.Pid)
    else:
        contexts = {
            "payment": payment,
            "projects": projects
        }
    return render(request,'deletePayment.html',contexts)
def exportToExcel():
    projects = Project.objects.all()