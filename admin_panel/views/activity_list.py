from django.shortcuts import render
from myapp.models import Activity
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_activity', login_url='/403')
def activity_list(request):
    # get all activities
    activities = Activity.objects.all()

    return render(request, 'activity_list.html', {'activities': activities})

