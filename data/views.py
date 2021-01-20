from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

app_name = 'data'

def data1(request):
    return render(request, 'data/django_study.html', {})

def data2(request):
    return render(request, 'data/lotto.html', {})

def data3(request):
    return render(request, 'data/study02.html', {})