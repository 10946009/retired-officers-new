from django.shortcuts import render
from myapp.models import Activity
from django.contrib.auth.decorators import login_required
# import login



@login_required(login_url='/login')
def activity_list(request):
    # get all activties
    activities = Activity.objects.all()


    return render(request, 'activity_list.html', {'activities': activities})

