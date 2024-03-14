from django.shortcuts import redirect
from user.models import Admin

def redirect_user(request):
    print(request.user.groups)
    if request.user.is_authenticated:
        
        # if user in admin-school group
        if request.user.groups.filter(name='admin-school').exists():
            return redirect('activity_list')
    return redirect('/')
