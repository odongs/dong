from django.urls import path

from . import views

app_name = 'data'

urlpatterns = [
    path('django/', views.data1, name='data/django'),
    path('lotto/', views.data2, name='data/lotto'),
    path('study/', views.data3, name='data/study'),
]