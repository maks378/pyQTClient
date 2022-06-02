import sys
import datetime
import requests
import json
from requests.exceptions import HTTPError
from PyQt6 import uic, QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    ServerAdress = "http://localhost:5000"
    MessageID = 0
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('messanger.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        self.SendMessage()

    def SendMessage(self):
        UserName = self.lineEdit1.text()
        MessageText = self.lineEdit2.text()
        TimeStamp = str(datetime.datetime.today())
        msg = f"{{\"UserName\": \"{UserName}\", \"MessageText\": \"{MessageText}\", \"TimeStamp\": \"{TimeStamp}\"}}"
        # {"UserName": "RusAl", "MessageText": "Privet na 100 let", "TimeStamp": "2021-03-05T18:23:12"}
        print("Отправлено сообщение: " + msg)
        url = self.ServerAdress + "/api/Messanger"
        data = json.loads(msg) # str to json
        r = requests.post(url, json=data)
        # print(r.sttus_code, r.reason)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
