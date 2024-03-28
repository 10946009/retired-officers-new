from django.shortcuts import render
from myapp.models import ScoreLabel


def score_label_list(request):
    score_labels = ScoreLabel.objects.all()
    return render(request, "score_label_list.html", {"score_labels": score_labels})