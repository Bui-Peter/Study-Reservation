import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from .forms import DateForm
from .models import Date
# Create your views here.

def index(request):
    date = Date(study_date='2018-05-30', room_size=4)
    date.save()
    
    room_list = []

    result = "You are at the index"

    #Get rooms

    data = {'date' : date.study_date}
    room = {}
    
    
    try:
        #Get the html of all rooms
        response = requests.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupid=2142&gid=2142&capacity=0', data)
        html = BeautifulSoup(response.text, 'html.parser')

        try:
            #If no rooms are unavailable return the html response
            unavailable = html.find('div', class_='alert alert-warning').contents[0].strip()
            return HttpResponse(unavailable)

        except:
            #Put every room with it's dictionary
            #Key=Room
            #Value=Available Times
            for collection in html.find_all('fieldset'):
                room_number = collection.legend.contents[0].strip()
                room[room_number] = []
                #Append times to the room number
                for period in collection.find_all('label'):
                    room[room_number].append(period.contents[2].strip())

    except:
        raise Http404('Unable to retrieve data')


    room_list.append("Hi")
    context = {'given_date' : date,'room_list' : room}
    return render(request, 'api/index.html', context)

