import sys
import requests
import sqlite3
import datetime
import json
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PySide6.QtCore import QRect
from Perva import Ui_Form


class FirstWindow:
    city = 'London'

    def setCity(self):
        self.city = self.lineEdit.text()
        self.openMain()

    def openMain(self):
        self.form.close()
        self.form = QMainWindow()
        ui = Ui_Form()
        ui.setupUi(self.form)
        set_infoWin(ui, **get_weather(city=self.city))
        self.form.show()

    def setupUi(self, form: QMainWindow):
        self.form = form
        form.resize(320, 40)
        self.lineEdit = QLineEdit(form)
        self.lineEdit.setGeometry(QRect(10, 10, 250, 20))
        self.pushButton = QPushButton(form)
        self.pushButton.setGeometry(QRect(265, 10, 45, 20))
        self.pushButton.setText("accept")
        self.pushButton.clicked.connect(self.setCity)


def set_infoWin(form: Ui_Form, **kwargs):
    dich = {'cloud_pct': 0, 'temp': 0, 'feels_like': 0, 'humidity': 0, 'min_temp': 0,
            'max_temp': 0, 'wind_speed': 0, 'wind_degrees': 0, 'sunrise': 0,
            'sunset': 0, 'city': 'London'}
    dich.update(kwargs)
    now = datetime.datetime.now()
    form.label.setText(f"Сейчас {now.hour:0>2}:{now.minute:0>2}.")
    form.label_2.setText(f"Город: {dich['city']}")
    form.label_3.setText(str(dich["temp"])+"°")
    form.label_4.setText(f"Восход {datetime.datetime.fromtimestamp(dich['sunrise']).strftime('%H:%M')}. Закат {datetime.datetime.fromtimestamp(dich['sunset']).strftime('%H:%M')}.")
    form.label_5.setText("Ветер: " + " " + str(dich["wind_speed"]) + "м/с " + ["Север", "Восток", "Юг", "Запад"][((dich["wind_degrees"] + 45) // 90) % 4])
    form.label_6.setText("Влажность: " + str(dich["humidity"]) + "%")


def get_weather(city='london'):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'ITskvCvFnJcN6G9kM+nShw==Ty1ElCMBsIhtTpQh'})
    if response.status_code == requests.codes.ok:
        res = {"city": city}
        res.update(json.loads(response.text))
        return res
    else:
        raise Exception("Error: " + str(response.status_code) + " " + response.text)


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = FirstWindow()
    ui.setupUi(win)

#    pcd = {'cloud_pct': 20, 'temp': 11, 'feels_like': 10, 'humidity': 73, 'min_temp': 9, 'max_temp': 12, 'wind_speed': 6.17, 'wind_degrees': 250, 'sunrise': 1699513643, 'sunset': 1699546876}
#    set_infoWin(ui, **pcd)
    win.show()
    sys.exit(app.exec())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
