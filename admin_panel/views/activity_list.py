from django.shortcuts import render
from myapp.models import Activity

def activity_list(request):
    # get all activties
    activities = Activity.objects.all()


    return render(request, 'activity_list.html', {'activities': activities})

