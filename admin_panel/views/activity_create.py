from django.shortcuts import redirect, render

from admin_panel.forms import ActivityForm
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_activity', login_url='/403')
def activity_create(request):

    if request.method == 'POST':
        form = ActivityForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('activity_list')
    else:
        form = ActivityForm()   

    return render(request, 'activity_create.html', {'form': form})

