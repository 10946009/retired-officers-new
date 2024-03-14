from django.utils import timezone
from django.shortcuts import render

from myapp.models import Activity


def index(request):

    # get all activity
    activities = Activity.objects.filter(activity_start_time__lte=timezone.now()).order_by("-activity_start_time")

    return render(request, "index.html", {"activities": activities})
