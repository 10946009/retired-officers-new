from django.shortcuts import render
from myapp.models import ScoreLabel
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

@permission_required('myapp.view_activity', login_url='/403')
def score_label_list(request):
    score_labels = ScoreLabel.objects.all()
    return render(request, "score_label_list.html", {"score_labels": score_labels})

@permission_required('myapp.view_activity', login_url='/403')
def score_label_delete(request, score_label_id):
    score_label = ScoreLabel.objects.get(id=score_label_id)
    print(score_label_id, score_label.id, score_label.label1, score_label.label2, score_label.label3)
    if request.method == 'POST':
        score_label.delete()
        return render(request, 'message.html', {'next':reverse('score_label_list'), 'message': '刪除成功'} )
