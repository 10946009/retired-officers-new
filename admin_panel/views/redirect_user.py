from django.shortcuts import redirect
from user.models import Admin

def redirect_user(request):
    '''
    google 登入後導向不同頁面
    school-admin -> activity_list, user -> index
    '''
    if request.user.is_authenticated:
        
        # if user in admin-school group
        if request.user.groups.filter(name='admin-school').exists():
            return redirect('activity_list')
    return redirect('index')
