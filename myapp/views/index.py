from django.shortcuts import render

from myapp.models import Activity


def index(request):

    # get all activity
    activities = Activity.objects.all()

    return render(request, "index.html", {"activities": activities})
