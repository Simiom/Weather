import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget
import time
import requests
import json
from geopy.geocoders import Nominatim


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('new.ui', self)

        self.vidipogod = {"clear ": "Ясно", "partly-cloudy": "Малооблачно", "cloudy ": "Облачно с прояснениями",
                          "overcast ": "Пасмурно", "partly-cloudy-and-light-rain": "Небольшой дождь",
                          "partly-cloudy-and-rain": "Дождь", "overcast-and-rain": " Сильный дождь",
                          "overcast-thunderstorms-with-rain": "Сильный дождь, гроза",
                          "cloudy-and-light-rain": "Небольшой дождь",
                          "overcast-and-light-rain": "Небольшой дождь", "cloudy-and-rain": "Дождь",
                          "overcast-and-wet-snow": "Дождь со снегом", "partly-cloudy-and-light-snow": "Небольшой снег",
                          "partly-cloudy-and-snow": "Снег", "overcast-and-snow": "Снегопад",
                          "cloudy-and-light-snow": "Небольшой снег", "overcast-and-light-snow": "Небольшой снег",
                          "cloudy-and-snow": "Снег"}
        self.day = 0
        self.hour = 0

        self.pokaz.clicked.connect(self.run)
        self.back.clicked.connect(self.strel)
        self.forward.clicked.connect(self.strel)
        self.chas.valueChanged.connect(self.update_weather)
        self.all_info = None
        self.mesto.setText("Москва")
        # self.send_request(self.mesto.text())
        # self.update_all()
        # self.chas.setValue(int(self.get_time().split()[3].split(":")[0]))

    def run(self):
        self.send_request(self.mesto.text())

        self.update_all()

    def update_all(self):
        self.pogoda.setText(self.vidipogod[self.get_forecast(0, self.hour)['condition']])

        pixmap = QPixmap(self.get_forecast(0, self.hour)['condition'] + ".png")
        self.pikcha.setPixmap(pixmap)
        self.pikcha.resize(pixmap.width(), pixmap.height())
        self.date.setText(
            self.get_time().split()[2] + " " + self.get_time().split()[1] + " " + self.get_time().split()[-1])
        self.lcdNumber.display(self.hour)
        self.show()

    def update_weather(self):
        self.hour = self.chas.value()
        self.update_all()

    def strel(self):
        if self.sender().text() == "<":
            pass
        else:
            pass

    def send_request(self, city):
        geolocator = Nominatim()
        location = geolocator.geocode(city)

        url = 'https://api.weather.yandex.ru/v1/forecast?lat={}&lon={}&extra=false'.format(location.latitude,
                                                                                                location.longitude)
        print(url)
        headers = {'X-Yandex-API-Key': 'd2c28be5-c612-4ddc-b5a2-d2b31e2baa71'}

        request = requests.get(url, headers=headers)
        self.all_info = json.loads(request.text)
        print(self.all_info["info"])

    def get_forecast(self, day, hour):
        if self.all_info != None:
            return self.all_info['forecasts'][day]['hours'][hour]

        else:
            print('send request before trying to get info')

    def get_time(self):
        if self.all_info != None:
            return time.ctime(self.all_info['fact']['obs_time'])
        else:
            print('send request before trying to get info')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
