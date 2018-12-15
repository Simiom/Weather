
import time
import requests
import json

from geopy.geocoders import Nominatim

all_info = None

def send_request(city):
    geolocator = Nominatim()
    location = geolocator.geocode(city)
    global all_info
    url = 'https://api.weather.yandex.ru/v1/forecast?info?lat={}&lon={}&extra=false'.format(location.latitude, location.longitude)
    headers = {'X-Yandex-API-Key': 'd2c28be5-c612-4ddc-b5a2-d2b31e2baa71'}

    request = requests.get(url, headers=headers)

    all_info = json.loads(request.text)



def get_forecast(day, hour):
    if all_info != None:
        return all_info['forecasts'][day]['hours'][hour]

    else:
        print('send request before trying to get info')


def get_time():
    if all_info != None:
        return time.ctime(all_info['fact']['obs_time'])
    else:
        print('send request before trying to get info')







send_request("Тюмень")
print(get_forecast(0,0))
print(get_time())