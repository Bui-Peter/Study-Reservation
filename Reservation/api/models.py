from django.db import models

import requests
from bs4 import BeautifulSoup

# Create your models here.
class Date(models.Model):
    study_date = models.DateTimeField('study date') 
    
class Rooms(models.Model):
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


   # STUDY_TIMES = retrieveRoomInfo()
