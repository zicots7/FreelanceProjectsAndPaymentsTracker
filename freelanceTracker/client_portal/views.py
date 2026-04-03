from django.shortcuts import render,redirect
from accounts.decorators import client_required
from Project.models import Project
from Milestone.models import Milestone
from Payment.models import Payment
from Logs.mongoDB import collection
from datetime import datetime
import uuid
@client_required
def dashboard(request):
    return render(request,'clientDashboard.html')
@client_required
def downloadInvoice(request,id):
    projects = Project.objects.get(Pid=id)
    return redirect('invoice-request',id=projects.Pid)
@client_required
def clientProjectDetails(request,id):
    logs = collection.find({"project_id":id})
    projects = Project.objects.get(Pid=id)
    milestone = Milestone.objects.filter(project_name=projects)
    payments = Payment.objects.filter(milestone__in=milestone)
    total_paid = sum(p.amount_paid for p in payments)
    pending = projects.total_value - total_paid
    contexts = {
        "projects":projects,
        "milestones":milestone,
        "payments":payments,
        "pending":pending,
        "total_paid":total_paid,
        "logs":logs,
    }
    return render(request,'userView.html',contexts)
@client_required
def clientProjectList(request):
    client = request.user.client_profile
    projects = Project.objects.filter(client=client).order_by('-start_date')
    return render(request,'clientProjects.html',{'projects':projects})
@client_required
def client_addLogs(request,id):
    projects = Project.objects.get(Pid=id)
    if request.method =="POST":
        interaction_type = request.POST.get('interaction_type')
        log_id = str(uuid.uuid4())[:8]
        add_fields = {
            "log_id": log_id,
            "project_id":id,
            "messages":request.POST.get('messages'),
            "timestamp":datetime.now(),
            "tags":request.POST.get('tags'),
            "interaction_type":interaction_type,

            }
        if interaction_type =="revision_request":
            add_fields["details"] = {
                "message":request.POST.get('message'),
                "revision_number":request.POST.get('revision_number'),
                "affected_pages":request.POST.get('affected_pages','').split(','),
                "priority":request.POST.get('priority'),
            }
        elif interaction_type == 'contract':
            add_fields['details'] = {
                "contract_value": request.POST.get('contract_value'),
                "payment_terms": request.POST.get('payment_terms'),
                "deliverables": request.POST.get('deliverables', '').split(','),
                "signed_date": request.POST.get('signed_date'),
            }
        elif interaction_type == 'requirement':
            add_fields['details'] = {
                "description": request.POST.get('description'),
                "tech_preference": request.POST.get('tech_preference'),
                "budget_flexible": request.POST.get('budget_flexible') == 'on',
                "deadline_flexible": request.POST.get('deadline_flexible') == 'on',
            }
        elif interaction_type == 'dispute':
            add_fields['details'] = {
                "reason": request.POST.get('reason'),
                "amount_disputed": request.POST.get('amount_disputed'),
                "resolution_status": "pending",
            }
        elif interaction_type == 'general_note':
            add_fields['details'] = {
                "message": request.POST.get('message'),
                "tags": request.POST.get('tags', '').split(','),
            }
        logs=collection.insert_one(add_fields)
        return redirect('client-project-details',id=projects.Pid)
    return render(request, 'client_addLogs.html', {'projects':projects})
@client_required
def client_deleteLogs(request,id,log_id):
    projects = Project.objects.get(Pid=id)
    if request.method =="POST":
        collection.delete_one({"log_id":log_id})
    return redirect('client-project-details',id=projects.Pid)