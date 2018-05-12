import requests
from bs4 import BeautifulSoup


data = {'date' : '2018-05-12'}

response = requests.get('https://gmu.libcal.com/spaces/accessible/ajax/group?prevGroupId=2142&gid=2142&capacity=0', data)
timeSlotHTML = response.text

soup = BeautifulSoup(timeSlotHTML, 'html.parser')

room = {}
for collection in soup.find_all('fieldset'):
    newRoom = collection.legend.contents[0].strip()
    room[newRoom] = []
    for period in collection.find_all('label'):
        room[newRoom].append(period.contents[2].strip())
    
date = soup.fieldset.p.string


print(soup.prettify())
print(room)
