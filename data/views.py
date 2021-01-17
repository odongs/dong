from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

app_name = 'data'

@login_required(login_url='common:login')
def data1(request):
    return render(request, 'data/django_study.html', {})

@login_required(login_url='common:login')
def data2(request):
    return render(request, 'data/lotto.html', {})

@login_required(login_url='common:login')
def data3(request):
    return render(request, 'data/study02.html', {})