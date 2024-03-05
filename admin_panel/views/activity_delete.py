from django.shortcuts import redirect, render
from myapp.models import Activity
from admin_panel.forms import ActivityForm

def activity_delete(request, activity_id):
    activity = Activity.objects.get(id=activity_id)

    if request.method == 'POST':
        activity.delete()
            
        return redirect('activity_list')
                    
    return render(request, 'activity_delete.html', {'activity': activity})

