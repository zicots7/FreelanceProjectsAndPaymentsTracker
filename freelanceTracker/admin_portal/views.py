from django.shortcuts import render,redirect
from accounts.decorators import *
from accounts.decorators import admin_required,demo_readonly


@admin_required
@demo_readonly
def admin_portal(request):
    return render(request, 'admin_portal.html')

@admin_required
@demo_readonly
def invoice(request):
    pass

