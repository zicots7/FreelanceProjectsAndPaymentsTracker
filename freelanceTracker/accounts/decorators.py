from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps

def admin_required(view_func):
    """
    # not logged in → login page
   # logged in but not admin → login page
   # admin → allow
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts')
        if request.user.role != 'admin':
            return redirect('accounts')
        return view_func(request, *args, **kwargs)
    return wrapper

def demo_readonly(view_func):
    """
this function particularly bypasses all the restrictions to user give access as demo account
 where user can interact with everything see everything but will not  be able to change anything
    :param view_func:
    :return: return to the current page with demo account notification
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_demo:
            if request.method == 'POST':
                messages.warning(
                    request,
                    "Demo accounts cannot make changes. Login with real credentials."
                )
                return redirect(request.path)
        return view_func(request, *args, **kwargs)
    return wrapper
def client_required(view_func):
    """
    # not logged in → login page
    # logged in but not client → login page
     # client → allow
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts')
        if request.user.role != 'client':
            return redirect('accounts')
        return view_func(request, *args, **kwargs)
    return wrapper

