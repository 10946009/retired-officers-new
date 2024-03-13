from django.shortcuts import redirect
from user.models import Admin

def redirect_user(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'admin'):
            return redirect('activity_list')
    return redirect('/')
