import datetime
import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import DateForm
from .models import Date

def index(request):
    size = 2
    if request.method == "POST":
        size = int(request.POST['size'])
    
    #default date is today
    date = Date(study_date=str(datetime.date.today()), room_size=size)
    date.save()
    
    room_list = []

    #Get rooms
    #gid:
    #   lobby(0) = 2142
    #   2 = 2116
    #   4 = 2117
    #   6 = 2118
    #   8 = 2119
    gid = {0 : 2142,  2 : 2116, 4 : 2117, 6 : 2118, 8 : 2119}
    data = {'gid' : gid[date.room_size], 'date' : date.study_date}
    room = {}
    
    
    try:
        #Get the html of all rooms
        response = requests.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupid=2142', data)
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

    context = {'given_date' : date,'room_list' : room}
    return render(request, 'api/index.html', context)
