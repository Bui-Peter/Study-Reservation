from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import DateForm

# Create your views here.

def index(request):
    return HttpResponse("Hello world. You are at the index")

def get_date(request):
    if request.method == 'POST':
        form = DateForm(request.POST)

        if form.is_valid():
#            form.cleaned_data
            
=======
            return HttpResponse(str(form.cleaned_data))

    else:
        form = DateForm()

    return render(request, 'date.html', {'form' : form})

