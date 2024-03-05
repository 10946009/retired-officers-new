from django.shortcuts import redirect, render

from admin_panel.forms import ActivityForm

def activity_create(request):

    if request.method == 'POST':
        form = ActivityForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('activity_list')
    else:
        form = ActivityForm()   

    return render(request, 'activity_create.html', {'form': form})

