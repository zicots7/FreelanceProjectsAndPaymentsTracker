from django.shortcuts import render,redirect
from accounts.decorators import *
from accounts.decorators import admin_required


@admin_required
def admin_portal(request):
    return render(request, 'admin_portal.html')

@admin_required
def invoice(request):
    pass

