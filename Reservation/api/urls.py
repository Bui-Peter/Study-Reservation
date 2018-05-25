from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('date', views.get_date, name='get_date')
]
