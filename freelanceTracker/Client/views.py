from django.shortcuts import render,redirect
from .form import ClientForm
from .models import Client
from django.contrib.auth import get_user_model
from accounts.decorators import admin_required
User = get_user_model()
@admin_required
def Client_list(request):
    """
      this functions returns the client list.
      return: returns client list
      """

    client = Client.objects.all()
    return render(request,'clientList.html',{"clients":client})
@admin_required
def add_client(request):
    """
      this functions performs client addition to the client list.
      return: client form
      """
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                role = 'client',
            )
            client = form.save(commit=False)
            client.user = user
            client.save()
            return redirect("add_client")
    else:
        form = ClientForm()
    return render(request,'addClient.html',{'form':form})
@admin_required
def delete_client(request,id):
    """
    this functions performs client deletion from client list fetching value by id
    return : client remaining list after performing deletion
    """
    client = Client.objects.get(id=id)
    if request.method == "POST":
        client = Client.objects.get(id=id)
        client.user.delete()
        return redirect("client_list")
    return render(request,'delete.html',{"client":client})
@admin_required
def update_client(request,id):
    """
       this functions performs client updation to the client list fetching the client by id.
       return: returns clinet form and updated client details
       """
    client = Client.objects.select_related('user').get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            #updating exsiting customer fields separately
            if form.cleaned_data.get('username'):
                client.user.username = form.cleaned_data['username']
            if form.cleaned_data.get('password'):
                client.user.password = form.cleaned_data['password']
            client.user.save()
            return redirect('client_list')
    else:
        #pre-fill form with existing data
        form = ClientForm(instance=client)
        #manually setting initial the username and passwoerd form customer database
        form.fields['username'].initial = client.user.username
        form.fields['password'].initial = ''# not pre-filling password for security reasons
    return render(request,'update.html',{'form':form,'client':client})


