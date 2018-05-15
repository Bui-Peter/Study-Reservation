from django.db import models

import requests
from bs4 import BeautifulSoup

# Create your models here.
class Date(models.Model):
    study_date = models.DateTimeField('study date')
    
    #What is study_date?
    def retrieveRoomInfo(cls):
        data = {'data' : cls.date}
        room = ()

        try:
            response = reponse.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupid=2142&gid=2142&capacity=0', data)
            html = BeautifulSoup(response.text, 'html.parser')

    STUDY_TIMES = retrieveRoomInfo()
