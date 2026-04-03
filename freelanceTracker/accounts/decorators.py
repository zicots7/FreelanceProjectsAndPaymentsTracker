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

