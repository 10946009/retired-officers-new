from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
def veteran(request):
    return redirect(reverse('veteran'))

def not_open(request):
    return HttpResponse("尚未開放")