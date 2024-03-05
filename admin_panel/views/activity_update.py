from django.shortcuts import redirect, render

from admin_panel.forms import ActivityForm
from myapp.models import Activity

def activity_update(request, activity_id):
    activity = Activity.objects.get(id=activity_id)

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)

        if form.is_valid():
            form.save() 
            
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
                    
    return render(request, 'activity_update.html', {'form': form, 'activity': activity})

