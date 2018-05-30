import datetime
import requests
from django.db import models
from bs4 import BeautifulSoup

# Create your models here.
class Date(models.Model):
    
    '''
    TODO:
        Rework the method to work withn tuples.
    '''
    def retrieveRoomInfo(cls):
        data = {'data' : cls.date}
        room = ()

        try:
            response = reponse.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupid=2142&gid=2142&capacity=0', data)
            html = BeautifulSoup(response.text, 'html.parser')

            try:
                unavailable = html.find('div', class_='alert alert-warning').contents[0].strip()
                print(unavailable)
            except:
                for collection in html.find_all('fieldset'):
                    newroom = collection.legend.contents[0].strip()
                    room[newRoom] = []
                    for period in collection.find_all('label'):
                        room[newRoom].append(period.contents[2].strip())

        except:
            print('Unable to retrieve data')

        return room


    ROOM_SIZES = (
        (2, "2"),
        (4, "4"),
        (6, "6"),
        (8, "8"),
    )

    study_date = models.DateField(default=datetime.date.today) 
    room_size = models.IntegerField(choices=ROOM_SIZES)

    #Returns as "date - room". Example: "2018-05-26 - 8"
    def __str__(self):
        return str(self.study_date) + " - " + str(self.room_size)

class Room(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)
    room_number = models.CharField(max_length=4, default="0000")

    def __str__(self):
        return str(self.date) + " - " + str(self.room_number)

class Time(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    study_time = models.TimeField()

    def __str__(self):
        return str(self.room) + " - " + str(self.study_time)
