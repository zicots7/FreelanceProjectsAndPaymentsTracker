from django.core.checks import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, get_user_model
def login_view(request):
    """

    :param request: POST request as parameter
    :return: authentication form
    """
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (
            username=username,
            password=password
        )
            if user:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_portal')
                else:
                    return redirect('client-dashboard')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})
def demo_login(request, role):
    try:
        User = get_user_model()

        if role == 'admin':
            user = User.objects.get(username='demo_admin')
        else:
            user = User.objects.get(username='demo_client')

        login(request, user)

        if role == 'admin':
            return redirect('admin_portal')
        else:
            return redirect('client_portal')

    except User.DoesNotExist:
        messages.error(request, "Demo account not available")
        return redirect('login')
def logout_view(request):
    """

    :param request: takes POST request
    :return: return to accounts login page after calling logout function
    """
    if request.method == "POST":
        logout(request)
        return redirect('accounts')
    return redirect('accounts')