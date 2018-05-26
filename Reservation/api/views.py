from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import DateForm

# Create your views here.

def index(request):
    return HttpResponse("Hello world. You are at the index")

def get_date(request):
    return HttpResponse("Getting the date")

