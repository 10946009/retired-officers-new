from django.shortcuts import redirect
from django.http import HttpResponse
def veteran(request):
    return redirect('index')

def not_open(request):
    return HttpResponse("尚未開放")