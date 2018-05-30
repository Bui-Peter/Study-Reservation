from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import DateForm

# Create your views here.

def index(request):
    date = Date(study_date='2018-05-30', room_size=4)
    date.save()

    result = "You are at the index"

'''
    try: 
        response = requests.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupId=2142&gid=2142&capacity=0', data)
        html = BeautifulSoup(response.text, 'html.parser')

        try:
            unavailable = html.find('div', class_='alert alert-warning').contents[0].strip()

            resut = unavailable

        except:
            for collection in html.find_all('fieldset'):
                newRoom = collection.legend.contents[0].strip()
                room[newroom] = []
                for period in collection.find_all('label'):
                    room[newRoom].append(period.contents[2].strip())

    except:
       result = "Unable to retrieve data"
'''

    return HttpResponse(result)

def get_date(request):
    return HttpResponse("Getting the date")


'''
    Methods
'''

def retrieveRoomInfo(self):
    data = {'date' : self.date}
    room = {}
    try:
        #Get then data
        response = requests.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupId=2142&gid=2142&capacity=0', data)
        html = BeautifulSoup(response.text, 'html.parser')

        #Unavailability
        try:
            unavailable = html.find("div", class_="alert alert-warning").contents[0].strip()
            print(unavailable)
        
        except:
            #Assign Room
            for collection in html.find_all('fieldset'):
                newRoom = collection.legend.contents[0].strip()
                room[newRoom] = []
                for period in collection.find_all('label'):
                    room[newRoom].append(period.contents[2].strip())

    except:
        print("Unable to retrieve data")
    
    return room
