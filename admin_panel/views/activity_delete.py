from django.shortcuts import redirect, render
from myapp.models import Activity
from admin_panel.forms import ActivityForm
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_activity', login_url='/403')
def activity_delete(request, activity_id):
    activity = Activity.objects.get(id=activity_id)

    if request.method == 'POST':
        activity.delete()
            
        return redirect('activity_list')
                    
    return render(request, 'activity_delete.html', {'activity': activity})

