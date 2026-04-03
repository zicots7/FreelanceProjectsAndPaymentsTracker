from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
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
def logout_view(request):
    """

    :param request: takes POST request
    :return: return to accounts login page after calling logout function
    """
    if request.method == "POST":
        logout(request)
        return redirect('accounts')
    return redirect('accounts')