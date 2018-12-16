import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget
import time
import requests
import json
from geopy.geocoders import Nominatim
import datetime
from PyQt5.QtCore import Qt
from new import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(262, 464)
        Form.setAutoFillBackground(False)
        self.pokaz = QtWidgets.QPushButton(Form)
        self.pokaz.setGeometry(QtCore.QRect(180, 4, 81, 23))
        self.pokaz.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pokaz.setAutoFillBackground(False)
        self.pokaz.setStyleSheet("")
        self.pokaz.setObjectName("pokaz")
        self.mesto = QtWidgets.QLineEdit(Form)
        self.mesto.setEnabled(True)
        self.mesto.setGeometry(QtCore.QRect(0, 5, 171, 20))
        self.mesto.setObjectName("mesto")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 300, 261, 146))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.data_layout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.data_layout_2.setContentsMargins(0, 0, 0, 0)
        self.data_layout_2.setObjectName("data_layout_2")
        self.temp2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp2.setFont(font)
        self.temp2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp2.setObjectName("temp2")
        self.data_layout_2.addWidget(self.temp2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.data_layout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.temp = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp.setFont(font)
        self.temp.setObjectName("temp")
        self.data_layout_2.addWidget(self.temp, 1, 1, 1, 1)
        self.wind_speed_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wind_speed_2.setFont(font)
        self.wind_speed_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wind_speed_2.setObjectName("wind_speed_2")
        self.data_layout_2.addWidget(self.wind_speed_2, 3, 0, 1, 1)
        self.pressure_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pressure_2.setFont(font)
        self.pressure_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_2.setObjectName("pressure_2")
        self.data_layout_2.addWidget(self.pressure_2, 5, 0, 1, 1)
        self.temp_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp_2.setFont(font)
        self.temp_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_2.setObjectName("temp_2")
        self.data_layout_2.addWidget(self.temp_2, 1, 0, 1, 1)
        self.davl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.davl.setFont(font)
        self.davl.setObjectName("davl")
        self.data_layout_2.addWidget(self.davl, 5, 1, 1, 1)
        self.wind_speed = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wind_speed.setFont(font)
        self.wind_speed.setObjectName("wind_speed")
        self.data_layout_2.addWidget(self.wind_speed, 3, 1, 1, 1)
        self.faketemp = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.faketemp.setFont(font)
        self.faketemp.setObjectName("faketemp")
        self.data_layout_2.addWidget(self.faketemp, 2, 1, 1, 1)
        self.vlaj = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vlaj.setFont(font)
        self.vlaj.setObjectName("vlaj")
        self.data_layout_2.addWidget(self.vlaj, 4, 1, 1, 1)
        self.date = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date.setFont(font)
        self.date.setText("")
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.data_layout_2.addWidget(self.date, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pikcha = QtWidgets.QLabel(Form)
        self.pikcha.setGeometry(QtCore.QRect(71, 90, 120, 126))
        self.pikcha.setText("")
        self.pikcha.setObjectName("pikcha")
        self.chas = QtWidgets.QSlider(Form)
        self.chas.setGeometry(QtCore.QRect(0, 270, 160, 22))
        self.chas.setMaximum(23)
        self.chas.setOrientation(QtCore.Qt.Horizontal)
        self.chas.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.chas.setObjectName("chas")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 262, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(110, 242, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.pogoda = QtWidgets.QLabel(Form)
        self.pogoda.setGeometry(QtCore.QRect(6, 30, 251, 61))
        self.pogoda.setText("")
        self.pogoda.setAlignment(QtCore.Qt.AlignCenter)
        self.pogoda.setObjectName("pogoda")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(0, 110, 21, 31))
        self.back.setObjectName("back")
        self.forward = QtWidgets.QPushButton(Form)
        self.forward.setGeometry(QtCore.QRect(240, 110, 21, 31))
        self.forward.setObjectName("forward")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(230, 270, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Погода"))
        self.pokaz.setText(_translate("Form", "Показать"))
        self.temp2.setText(_translate("Form", "Ощущается как:"))
        self.label_4.setText(_translate("Form", "Влажность:"))
        self.temp.setText(_translate("Form", "TextLabel"))
        self.wind_speed_2.setText(_translate("Form", "Скорость ветра:"))
        self.pressure_2.setText(_translate("Form", "Давление:"))
        self.temp_2.setText(_translate("Form", "Температура:"))
        self.davl.setText(_translate("Form", "TextLabel"))
        self.wind_speed.setText(_translate("Form", "TextLabel"))
        self.faketemp.setText(_translate("Form", "TextLabel"))
        self.vlaj.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "Время"))
        self.back.setText(_translate("Form", "<"))
        self.forward.setText(_translate("Form", ">"))
        self.label_6.setText(_translate("Form", "ч."))




class MyWidget(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(262, 464)

        self.vidipogod = {"clear": "Ясно", "partly-cloudy": "Малооблачно", "cloudy": "Облачно с прояснениями",
                          "overcast": "Пасмурно", "partly-cloudy-and-light-rain": "Небольшой дождь",
                          "partly-cloudy-and-rain": "Дождь", "overcast-and-rain": "Сильный дождь",
                          "overcast-thunderstorms-with-rain": "Сильный дождь, гроза",
                          "cloudy-and-light-rain": "Небольшой дождь",
                          "overcast-and-light-rain": "Небольшой дождь", "cloudy-and-rain": "Дождь",
                          "overcast-and-wet-snow": "Дождь со снегом", "partly-cloudy-and-light-snow": "Небольшой снег",
                          "partly-cloudy-and-snow": "Снег", "overcast-and-snow": "Снегопад",
                          "cloudy-and-light-snow": "Небольшой снег", "overcast-and-light-snow": "Небольшой снег",
                          "cloudy-and-snow": "Снег"}

        self.hour = 0

        self.pokaz.clicked.connect(self.run)
        self.back.clicked.connect(self.strel)
        self.forward.clicked.connect(self.strel)
        self.chas.valueChanged.connect(self.update_weather)
        self.all_info = None
        self.sdvig = 0

        self.mesto.setText("Москва")
        self.send_request(self.mesto.text())
        self.day = int(self.get_date(0)[-1])
        self.hour = int(self.get_time().split()[3].split(":")[0])
        self.update_all()
        self.chas.setValue(int(self.get_time().split()[3].split(":")[0]))

    def run(self):
        self.sdvig = 0
        self.send_request(self.mesto.text())
        self.day = int(self.get_date(0)[-1])
        self.chas.setValue(int(self.get_time().split()[3].split(":")[0]))
        self.update_all()

    def update_all(self):
        self.pogoda.setText(self.vidipogod[self.get_forecast(0 + self.sdvig, self.hour)['condition']])

        pixmap = QPixmap(self.get_forecast(0 + self.sdvig, self.hour)['condition'] + ".png")
        self.pikcha.setPixmap(pixmap)
        self.pikcha.resize(pixmap.width(), pixmap.height())

        self.date.setText(
            str(self.day) + "." + self.get_date(self.sdvig)[1] + "." + self.get_date(self.sdvig)[0])
        self.lcdNumber.display(self.hour)
        self.temp.setText(str(self.get_forecast(self.sdvig, self.hour)["temp"]))
        self.faketemp.setText(str(self.get_forecast(self.sdvig, self.hour)["feels_like"]))
        self.wind_speed.setText(str(self.get_forecast(self.sdvig, self.hour)["wind_speed"]) + " м/с")
        self.vlaj.setText(str(self.get_forecast(self.sdvig, self.hour)["humidity"]) + " %")
        self.davl.setText(str(self.get_forecast(self.sdvig, self.hour)["pressure_mm"]) + " мм.рт.ст.")

        self.show()

    def update_weather(self):
        if self.day == int(self.get_date(0)[-1]):
            if self.chas.value() < int(self.get_time().split()[3].split(":")[0]):
                self.chas.setValue(self.hour)
        self.hour = self.chas.value()
        self.update_all()

    def strel(self):
        if self.sender().text() == "<":
            if self.sdvig - 1 >= 0:

                self.day -= 1
                self.sdvig -= 1
                if self.sdvig == 0:
                    self.chas.setValue(int(self.get_time().split()[3].split(":")[0]))
        else:
            if self.sdvig + 1 <= 2:
                self.day += 1
                self.sdvig += 1
                self.chas.setValue(0)
        self.update_all()

    def send_request(self, city):
        geolocator = Nominatim()
        location = geolocator.geocode(city)

        url = 'https://api.weather.yandex.ru/v1/forecast?lat={}&lon={}&extra=false'.format(location.latitude,
                                                                                           location.longitude)

        headers = {'X-Yandex-API-Key': 'd2c28be5-c612-4ddc-b5a2-d2b31e2baa71'}

        request = requests.get(url, headers=headers)
        self.all_info = json.loads(request.text)

    def get_forecast(self, day, hour):
        if self.all_info != None:
            return self.all_info['forecasts'][day]['hours'][hour]

        else:
            print('send request before trying to get info')

    def get_time(self):
        now = time.ctime(time.time() + (time.altzone + 3600) + int(self.all_info["info"]["tzinfo"]["offset"]))
        return now

    def get_date(self, offset):
        return self.all_info['forecasts'][offset]['date'].split('-')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
