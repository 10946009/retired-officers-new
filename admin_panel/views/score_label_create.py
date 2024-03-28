from django.shortcuts import redirect, render

from admin_panel.forms import ScoreLabelForm
from user.models import ActivityStudents
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
@permission_required('myapp.view_activity', login_url='/403')

def score_label_create(request):
    if request.method == "POST":
        form = ScoreLabelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "message.html", {"next":reverse('score_label_list'), "message": "新增成功"})
    else:
        form = ScoreLabelForm()
    return render(request, "score_label_create.html", {"form": form})