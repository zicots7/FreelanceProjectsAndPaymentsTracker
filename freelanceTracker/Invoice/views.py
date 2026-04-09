from django.shortcuts import render,redirect,get_object_or_404
from accounts.decorators import admin_required,client_required,demo_readonly
from Project.models import Project
from django.http import HttpResponse
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

@client_required
@demo_readonly
def clientinvoiceDownload(request,id):
    projects = get_object_or_404(
        Project.objects.select_related('client'), Pid=id
    )
    print(projects.description)
    pdfUri = os.getenv("FREELANCETRACKERPDF")
    invoice_data = {
        "ClientName": str(projects.client),
        "ProjectName": str(projects.title),
        "Amount": projects.total_value,
        "Date": str(datetime.now()),
        "ProjectDescription": str(projects.description),

    }
    try:
        pdfRequest = requests.post(
            pdfUri,
            json=invoice_data,
            timeout=10
        )
        if pdfRequest.status_code == 200:
            http_response = HttpResponse(
                pdfRequest.content,
                content_type='application/pdf'
            )
            http_response['Content-Disposition'] = (
                f'attachment; filename="invoice_{projects.client}_{projects.Pid}.pdf"'
            )
            return http_response
    except requests.exceptions.ConnectionError:
        return HttpResponse(
            "Invoice service unavailable. Please try again later.",
            status=503
        )



@admin_required
def invoiceDownload(request,id):
    projects = get_object_or_404(
        Project.objects.select_related('client'),Pid=id
    )
    print(projects.description)
    pdfUri = os.getenv("FREELANCETRACKERPDF")
    invoice_data = {
        "ClientName": str(projects.client),
        "ProjectName": str(projects.title),
        "Amount": projects.total_value,
        "Date": str(datetime.now()),
        "ProjectDescription": str(projects.description),

    }
    try:
        pdfRequest = requests.post(
            pdfUri,
            json=invoice_data,
            timeout=10
        )
        if pdfRequest.status_code == 200:
            http_response = HttpResponse(
                pdfRequest.content,
                content_type='application/pdf'
            )
            http_response['Content-Disposition'] = (
                f'attachment; filename="invoice_{projects.client}_{projects.Pid}.pdf"'
            )
            return http_response
    except requests.exceptions.ConnectionError:
        return HttpResponse(
            "Invoice service unavailable.Please try again later.",
            status=503
        )
