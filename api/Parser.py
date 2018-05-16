import requests
import datetime
from bs4 import BeautifulSoup

class Parser():
    
    '''
        room capacity ID's:
            Lobby: 2142
            2-People: 2116
            4-People: 2117
            6-People: 2118
            8-People: 2119
    '''

    roomID = {'lobby' : 2142, 2 : 2116, 4 : 2217, 6 : 2118, 8 : 2119}

    def __init__(self, date, numberOfPeople):
        self.date = date
        self.hasData = False
        self.roomCap = self.roomID[numberOfPeople]
        self.room = self.retrieveRoomInfo()

    '''
        Returns in the format:
            Room: 1205
                Times: 4:00pm - 4:30pm | 6:30pm - 7:00pm |
            Room: 1204
                Times: ...
    '''
    def __str__(self):
        result = ''
        for rooms in self.room.keys():
            availableTime = ''
            for time in self.room[rooms]:
               availableTime += str(time) + " | "
            result += 'Room: ' + str(rooms) + '\n\t' + 'Times: ' + availableTime + '\n'
        return result

    '''
        Retrieves the html of libcal on the date when initialized.
        Assigns the rooms as a key to a list of available times

        return: parsed room hashmap (room number : available times(list))

        returns empty room if error occurs (can't get room)
    '''
    def retrieveRoomInfo(self):
        data = {'gid' : self.roomCap, 'date' : self.date}
        room = {}
        try:
            #Get then data
            response = requests.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupId=2142&capacity=0', data)
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
