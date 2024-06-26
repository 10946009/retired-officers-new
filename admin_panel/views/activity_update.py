from django.shortcuts import redirect, render

from admin_panel.forms import ActivityForm
from myapp.models import Activity
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_activity', login_url='/403')
def activity_update(request, activity_id):
    '''
    Update activity
    '''
    activity = Activity.objects.get(id=activity_id)

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)

        if form.is_valid():
            form.save() 
            message = "活動資料更新成功"
            # return redirect(f'/admin_panel/activity_tool_menu/{activity_id}')
            return render(request, 'message.html', {'next': f'/admin_panel/activity_tool_menu/{activity_id}', 'message': message})
        else:
            message = "活動資料更新失敗"
            return render(request, 'message.html', {'next': f'/admin_panel/activity_update/{activity_id}', 'message': message})
    else:
        form = ActivityForm(instance=activity)
                    
    return render(request, 'activity_update.html', {'form': form, 'activity': activity})

