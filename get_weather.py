import datetime
import time
import requests
import json
from geopy.geocoders import Nominatim
from pytz import country_timezones

all_info = None

def send_request(city):
    geolocator = Nominatim()
    location = geolocator.geocode(city)
    global all_info
    url = 'https://api.weather.yandex.ru/v1/forecast?lat={}&lon={}&extra=false'.format(location.latitude, location.longitude)
    headers = {'X-Yandex-API-Key': 'd2c28be5-c612-4ddc-b5a2-d2b31e2baa71'}

    request = requests.get(url, headers=headers)

    all_info = json.loads(request.text)



def get_forecast(day, hour):
    if all_info != None:
        return all_info['forecasts'][day]['hours'][hour]

    else:
        print('send request before trying to get info')


def get_time():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d.%m.%Y %H")





send_request("London")
print(get_forecast(0,0))
print(get_time())
print(all_info['info'])
#1544832000