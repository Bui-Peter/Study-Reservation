from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import DateForm

# Create your views here.

def index(request):
    return HttpResponse("Hello world. You are at the index")

def get_date(request):
    if request.method == 'POST':
        form = DateForm(request.POST)

        if form.is_valid():
#            form.cleaned_data
            

