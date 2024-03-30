from django.shortcuts import  render
from myapp.models import ScoreLabel
from admin_panel.forms import ScoreLabelForm
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

@permission_required('myapp.view_activity', login_url='/403')
def score_label_create(request):
    '''
    Create a new score label
    '''
    if request.method == "POST":
        form = ScoreLabelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "message.html", {"next":reverse('score_label_list'), "message": "新增成功"})
    else:
        form = ScoreLabelForm()
    return render(request, "score_label_create.html", {"form": form})

@permission_required('myapp.view_activity', login_url='/403')
def score_label_update(request, score_label_id):
    '''
    score label update
    '''
    score_label = ScoreLabel.objects.get(id=score_label_id)
    if request.method == "POST":
        form = ScoreLabelForm(request.POST, instance=score_label)
        if form.is_valid():
            form.save()
            return render(request, "message.html", {"next":reverse('score_label_list'), "message": "修改成功"})
    else:
        form = ScoreLabelForm(instance=score_label)
    return render(request, "score_label_update.html", {"form": form})