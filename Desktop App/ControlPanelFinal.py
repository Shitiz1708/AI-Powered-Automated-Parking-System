import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot,QTimer
from PyQt5.QtGui import QImage,QPixmap
import cv2
from QR import scan
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
from firebase import firebase

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

result = {}

class FB:
    def __init__(self):
        fb = firebase.FirebaseApplication('https://parkitright-330d9.firebaseio.com/', None)
        print(fb)
        print("A")
        global result
        result = fb.get("/",None)
        print(result)


# def FirebaseAccess():
#         fb = firebase.FirebaseApplication('https://parkitright-330d9.firebaseio.com/', None)
#         print(fb)
#         print("A")
#         global result
#         result = fb.get("/",None)
#         print(result)
#         # self.fillValues()
#         # result = firebase1.get('/Lot_Id/1', None)
#         # print(result)


class Ui_ControlPanel(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # FirebaseAccess()
        self.setupUi(self)
        self.default()
        global result
        self.result = result
        # print(self.result)

        self.updateValues()
        # self.fillValues()
        # self.fillBookings()
        # fb = FB()
        # self.setupCamera()
        # timer = QTimer(self)
        # timer.setInterval(int(30))
        # timer.timeout.connect(self.updateValues)
        # timer.start()
        self.updateValues()
    
    def updateValues(self):
        self.fillValues()
        self.fillBookings()
        fb = FB()
    
    def default(self):
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        self.lcdNumber_3.display(100)
    
    # def FirebaseAccess(self):
    #     fb = firebase.FirebaseApplication('https://parkitright-330d9.firebaseio.com/', None)
    #     print(fb)
    #     print("A")
    #     result = fb.get("/",None)
        # print(self.result)
        # self.fillValues()
        # result = firebase1.get('/Lot_Id/1', None)
        # print(result)
    
    def fillValues(self):
        
        self.available = self.result["Lot_Id"][1]["Available"]
        self.lcdNumber.display(self.available)
        self.lcdNumber_2.display(100-self.available)
        self.lcdNumber_3.display(100)

    def fillBookings(self):
        c=0
        self.tableWidget.setRowCount(0)
        print(self.result["Lot_Id"][1]["Bookings"])
        for i in self.result["Lot_Id"][1]["Bookings"]:
            print(i)
            if i==None:
                pass
            else:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(i["Time"]))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i["Vehicle No"])))
                c=c+1



    def setupCamera(self):
        self.capture = cv2.VideoCapture("lane.gif")
        timer = QTimer(self)
        timer.setInterval(int(1000/30))
        timer.timeout.connect(self.get_frame)
        timer.start()
    
    def get_frame(self):
        _,frame = self.capture.read()
        print(frame)
        # frame = self.process_frame(frame1)
        image = QImage(frame, *frame.shape[1::-1], QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)
        self.image.setPixmap(pixmap)


    #Here all processing will be done
    def process_frame(self):
        return
    
    def close(self):
        self.close()

    def QRScanner(self):
        # self.image.setText("Window Closed")
        # cv2.destroyAllWindows()
        scan()
        self.tableWidget.removeRow(0)
        QtWidgets.QMessageBox.information(self, 'Success', 'Booking Confirmed')



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 497)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 281, 51))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 57 11pt \"Ubuntu\";\n"
"font-size:30px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 80, 251, 241))
        self.image.setStyleSheet(" border-top: 10px, white, double;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.image.setObjectName("image")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 70, 261, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_5.addWidget(self.lcdNumber_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("color:rgb(255, 255, 255);\n"
"text-align:center;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("color:rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("color:rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(self.QRScanner)
        self.pushButton.clicked.connect(self.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PARK_IT_RIGHT"))
        self.image.setText(_translate("MainWindow", "Live CCTV Footage With CV"))
        self.label_3.setText(_translate("MainWindow", "Available Spaces"))
        self.label_4.setText(_translate("MainWindow", "Reserved Spaces"))
        self.label_5.setText(_translate("MainWindow", "Total Spaces        "))
        self.label_6.setText(_translate("MainWindow", "Bookings"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vehicle No."))
        self.pushButton_2.setText(_translate("MainWindow", "QR Code Scanner"))
        self.pushButton.setText(_translate("MainWindow", "Close"))




if __name__ == '__main__':
    # FirebaseAccess()
    fb = FB()
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_ControlPanel()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())
