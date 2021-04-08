# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'godseye.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from modules.ge_emailcheck import check
from modules.ge_geoiplookup import geoipLookup
from modules.ge_accountfinder import holohe
from modules.ge_whatsmyname import whatsmyname
from modules.ge_haveibeenpwned import haveibeenpwned

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QBrush, QColor

class Ui_MainWindow(object):

    previousEmail = ""
    previousIp = ""
    previousNick = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("God's Eye")
        MainWindow.setFixedSize(1100, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(40, 42, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.email.setStyleSheet("background-color: rgb(68, 71, 90);\n"
"color: rgb(243, 243, 243);")
        self.email.setObjectName("email")
        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(140, 10, 113, 20))
        self.ip.setStyleSheet("background-color: rgb(68, 71, 90);\n"
"color: rgb(243, 243, 243);")
        self.ip.setObjectName("ip")
        self.nick = QtWidgets.QLineEdit(self.centralwidget)
        self.nick.setGeometry(QtCore.QRect(270, 10, 113, 20))
        self.nick.setStyleSheet("background-color: rgb(68, 71, 90);\n"
"color: rgb(243, 243, 243);")
        self.nick.setObjectName("nick")

        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(400, 10, 51, 23))
        self.search.setStyleSheet("background-color: rgb(80, 250, 123);")
        self.search.setObjectName("search")
        self.search.clicked.connect(lambda: self.Execute(self.email.text(), self.ip.text(), self.nick.text()))

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 111, 81))
        self.frame.setStyleSheet("background-color: rgb(68, 71, 90);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.trumail = QtWidgets.QCheckBox(self.frame)
        self.trumail.setGeometry(QtCore.QRect(10, 50, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.trumail.setFont(font)
        self.trumail.setStyleSheet("color:  rgb(248, 248, 242);")
        self.trumail.setObjectName("trumail")
        self.debounce = QtWidgets.QCheckBox(self.frame)
        self.debounce.setGeometry(QtCore.QRect(10, 30, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.debounce.setFont(font)
        self.debounce.setStyleSheet("color:  rgb(248, 248, 242);")
        self.debounce.setObjectName("debounce")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("color: rgb(241, 250, 140);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(140, 40, 241, 521))
        self.frame_2.setStyleSheet("background-color: rgb(68, 71, 90);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet("color: rgb(241, 250, 140);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_3.setObjectName("label_3")
        self.hostname = QtWidgets.QLabel(self.frame_2)
        self.hostname.setGeometry(QtCore.QRect(10, 50, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.hostname.sizePolicy().hasHeightForWidth())
        self.hostname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.hostname.setFont(font)
        self.hostname.setStyleSheet("color: rgb(243, 243, 243);")
        self.hostname.setText("")
        self.hostname.setObjectName("hostname")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_4.setObjectName("label_4")
        self.asn = QtWidgets.QLabel(self.frame_2)
        self.asn.setGeometry(QtCore.QRect(10, 90, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.asn.sizePolicy().hasHeightForWidth())
        self.asn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.asn.setFont(font)
        self.asn.setStyleSheet("color: rgb(243, 243, 243);")
        self.asn.setText("")
        self.asn.setObjectName("asn")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_5.setObjectName("label_5")
        self.organization = QtWidgets.QLabel(self.frame_2)
        self.organization.setGeometry(QtCore.QRect(10, 130, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.organization.sizePolicy().hasHeightForWidth())
        self.organization.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.organization.setFont(font)
        self.organization.setStyleSheet("color: rgb(243, 243, 243);")
        self.organization.setText("")
        self.organization.setObjectName("organization")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_6.setObjectName("label_6")
        self.type = QtWidgets.QLabel(self.frame_2)
        self.type.setGeometry(QtCore.QRect(10, 170, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.type.setFont(font)
        self.type.setStyleSheet("color: rgb(243, 243, 243);")
        self.type.setText("")
        self.type.setObjectName("type")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_7.setObjectName("label_7")
        self.assignment = QtWidgets.QLabel(self.frame_2)
        self.assignment.setGeometry(QtCore.QRect(10, 210, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.assignment.sizePolicy().hasHeightForWidth())
        self.assignment.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.assignment.setFont(font)
        self.assignment.setStyleSheet("color: rgb(243, 243, 243);")
        self.assignment.setText("")
        self.assignment.setObjectName("assignment")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_8.setObjectName("label_8")
        self.continent = QtWidgets.QLabel(self.frame_2)
        self.continent.setGeometry(QtCore.QRect(10, 250, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.continent.sizePolicy().hasHeightForWidth())
        self.continent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.continent.setFont(font)
        self.continent.setStyleSheet("color: rgb(243, 243, 243);")
        self.continent.setText("")
        self.continent.setObjectName("continent")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 270, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_9.setObjectName("label_9")
        self.country = QtWidgets.QLabel(self.frame_2)
        self.country.setGeometry(QtCore.QRect(10, 290, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.country.sizePolicy().hasHeightForWidth())
        self.country.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.country.setFont(font)
        self.country.setStyleSheet("color: rgb(243, 243, 243);")
        self.country.setText("")
        self.country.setObjectName("country")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_10.setObjectName("label_10")
        self.region = QtWidgets.QLabel(self.frame_2)
        self.region.setGeometry(QtCore.QRect(10, 330, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.region.sizePolicy().hasHeightForWidth())
        self.region.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.region.setFont(font)
        self.region.setStyleSheet("color: rgb(243, 243, 243);")
        self.region.setText("")
        self.region.setObjectName("region")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_11.setObjectName("label_11")
        self.city = QtWidgets.QLabel(self.frame_2)
        self.city.setGeometry(QtCore.QRect(10, 370, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.city.sizePolicy().hasHeightForWidth())
        self.city.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.city.setFont(font)
        self.city.setStyleSheet("color: rgb(243, 243, 243);")
        self.city.setText("")
        self.city.setObjectName("city")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 390, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_12.setObjectName("label_12")
        self.latitude = QtWidgets.QLabel(self.frame_2)
        self.latitude.setGeometry(QtCore.QRect(10, 410, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.latitude.sizePolicy().hasHeightForWidth())
        self.latitude.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.latitude.setFont(font)
        self.latitude.setStyleSheet("color: rgb(243, 243, 243);")
        self.latitude.setText("")
        self.latitude.setObjectName("latitude")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 430, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_13.setObjectName("label_13")
        self.longitude = QtWidgets.QLabel(self.frame_2)
        self.longitude.setGeometry(QtCore.QRect(10, 450, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.longitude.sizePolicy().hasHeightForWidth())
        self.longitude.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.longitude.setFont(font)
        self.longitude.setStyleSheet("color: rgb(243, 243, 243);")
        self.longitude.setText("")
        self.longitude.setObjectName("longitude")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(10, 470, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_14.setObjectName("label_14")
        self.postalcode = QtWidgets.QLabel(self.frame_2)
        self.postalcode.setGeometry(QtCore.QRect(10, 490, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.postalcode.sizePolicy().hasHeightForWidth())
        self.postalcode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.postalcode.setFont(font)
        self.postalcode.setStyleSheet("color: rgb(243, 243, 243);")
        self.postalcode.setText("")
        self.postalcode.setObjectName("postalcode")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(400, 40, 391, 521))
        self.frame_3.setStyleSheet("background-color: rgb(68, 71, 90);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 371, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAcceptDrops(False)
        self.label_15.setStyleSheet("color: rgb(241, 250, 140);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.downloads = QtWidgets.QTableWidget(self.frame_3)
        self.downloads.setGeometry(QtCore.QRect(10, 30, 371, 481))
        self.downloads.setStyleSheet("")
        self.downloads.setObjectName("downloads")
        self.downloads.setColumnCount(4)
        self.downloads.setRowCount(0)
        stylesheet = "::section{Background-color:rgb(241, 250, 140);}"
        self.downloads.verticalHeader().setStyleSheet(stylesheet)
        self.downloads.horizontalHeader().setStyleSheet(stylesheet)
        item = QtWidgets.QTableWidgetItem()
        self.downloads.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.downloads.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.downloads.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.downloads.setHorizontalHeaderItem(3, item)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 140, 111, 421))
        self.frame_4.setStyleSheet("background-color: rgb(68, 71, 90);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAcceptDrops(False)
        self.label_16.setStyleSheet("color: rgb(241, 250, 140);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.accountsEmail = QtWidgets.QListWidget(self.frame_4)
        self.accountsEmail.setGeometry(QtCore.QRect(10, 30, 91, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountsEmail.sizePolicy().hasHeightForWidth())
        self.accountsEmail.setSizePolicy(sizePolicy)
        self.accountsEmail.setMovement(QtWidgets.QListView.Free)
        self.accountsEmail.setObjectName("accountsEmail")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(810, 40, 281, 521))
        self.frame_5.setStyleSheet("background-color: rgb(68, 71, 90);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(20, 10, 241, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAcceptDrops(False)
        self.label_17.setStyleSheet("color: rgb(241, 250, 140);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.accountsNickname = QtWidgets.QListWidget(self.frame_5)
        self.accountsNickname.setGeometry(QtCore.QRect(10, 30, 261, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountsNickname.sizePolicy().hasHeightForWidth())
        self.accountsNickname.setSizePolicy(sizePolicy)
        self.accountsNickname.setMovement(QtWidgets.QListView.Free)
        self.accountsNickname.setObjectName("accountsNickname")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(10, 580, 1081, 201))
        self.frame_6.setStyleSheet("background-color: rgb(68, 71, 90);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 1061, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAcceptDrops(False)
        self.label_18.setStyleSheet("color: rgb(241, 250, 140);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.breachesTable = QtWidgets.QTableWidget(self.frame_6)
        self.breachesTable.setGeometry(QtCore.QRect(10, 30, 1061, 161))
        self.breachesTable.setStyleSheet("")
        self.breachesTable.setObjectName("breachesTable")
        self.breachesTable.setColumnCount(7)
        self.breachesTable.setRowCount(0)
        stylesheet = "::section{Background-color:rgb(241, 250, 140);}"
        self.breachesTable.verticalHeader().setStyleSheet(stylesheet)
        self.breachesTable.horizontalHeader().setStyleSheet(stylesheet)
        self.breachesTable.setCornerButtonEnabled(False)
        self.breachesTable.horizontalHeader().setStretchLastSection(True)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.breachesTable.setHorizontalHeaderItem(6, item)
        self.credits = QtWidgets.QLabel(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(896, 10, 191, 21))
        self.credits.setStyleSheet("color: rgb(189, 147, 249);")
        self.credits.setObjectName("credits")
        self.frame.raise_()
        self.email.raise_()
        self.ip.raise_()
        self.nick.raise_()
        self.search.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.credits.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "God's Eye"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-MAIL"))
        self.ip.setPlaceholderText(_translate("MainWindow", "IP ADDRESS"))
        self.nick.setPlaceholderText(_translate("MainWindow", "NICKNAME"))
        self.search.setText(_translate("MainWindow", "SEARCH"))
        self.trumail.setText(_translate("MainWindow", "Trumail.io"))
        self.debounce.setText(_translate("MainWindow", "Debounce.io"))
        self.label.setText(_translate("MainWindow", "Disposable:"))
        self.label_2.setText(_translate("MainWindow", "IP Info from whatismyipaddress.com:"))
        self.label_3.setText(_translate("MainWindow", "Hostname:"))
        self.label_4.setText(_translate("MainWindow", "ASN:"))
        self.label_5.setText(_translate("MainWindow", "Organization:"))
        self.label_6.setText(_translate("MainWindow", "Type:"))
        self.label_7.setText(_translate("MainWindow", "Assignment:"))
        self.label_8.setText(_translate("MainWindow", "Continent:"))
        self.label_9.setText(_translate("MainWindow", "Country:"))
        self.label_10.setText(_translate("MainWindow", "State/Region:"))
        self.label_11.setText(_translate("MainWindow", "City:"))
        self.label_12.setText(_translate("MainWindow", "Latitude:"))
        self.label_13.setText(_translate("MainWindow", "Longitude:"))
        self.label_14.setText(_translate("MainWindow", "Postal Code:"))
        self.label_15.setText(_translate("MainWindow", "iknowwhatyoudownload.com:"))
        item = self.downloads.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Download Time"))
        item = self.downloads.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.downloads.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.downloads.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size"))
        self.label_16.setText(_translate("MainWindow", "Accounts:"))
        self.label_17.setText(_translate("MainWindow", "Accounts by nickname:"))
        self.label_18.setText(_translate("MainWindow", "haveibeenpwned.com:"))
        item = self.breachesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.breachesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Domain"))
        item = self.breachesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.breachesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Pwn Count"))
        item = self.breachesTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data Leaked"))
        item = self.breachesTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Breach Date"))
        item = self.breachesTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Description"))
        self.credits.setText(_translate("MainWindow", 'Made by Theos - <a href="http://github.com/Loiuy123" style="color: rgb(189, 147, 249)">github.com/Loiuy123</a>'))
        self.credits.setOpenExternalLinks(True)

    def showPopup(self, text):
        pass

    def Execute(self, _email = "", _ip = "", _nick = ""):

        if _email != "" and self.previousEmail != _email:
            self.previousEmail = _email

            #Check if email is disposable
            try:
                disposableList = check(_email)

                self.debounce.setCheckState(disposableList[0])
                self.trumail.setCheckState(disposableList[1])
            except:
                pass
            #Check accounts created using target email
            holoheList = holohe(_email)
            self.accountsEmail.clear()

            holoheAccIndex = 0
            for holoheAcc in holoheList:
                self.accountsEmail.addItem(holoheAcc)
                acc = self.accountsEmail.item(holoheAccIndex)
                acc.setForeground(QBrush(QColor(248, 248, 242)))    
                holoheAccIndex += 1

            #Check if email is pwned
            pwnedList = haveibeenpwned(_email)
            row = 0
            self.breachesTable.setRowCount(len(pwnedList["Breaches"]))
            if pwnedList != None:
                for i in range(len(pwnedList["Breaches"])):
                    self.breachesTable.setItem(row, 0, QtWidgets.QTableWidgetItem(pwnedList["Breaches"][row]["Name"]))
                    item = self.breachesTable.item(row, 0)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    self.breachesTable.setItem(row, 1, QtWidgets.QTableWidgetItem(pwnedList["Breaches"][row]["Domain"]))
                    item = self.breachesTable.item(row, 1)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    self.breachesTable.setItem(row, 2, QtWidgets.QTableWidgetItem(pwnedList["Breaches"][row]["Title"]))
                    item = self.breachesTable.item(row, 2)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    self.breachesTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(pwnedList["Breaches"][row]["PwnCount"])))
                    item = self.breachesTable.item(row, 3)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    self.breachesTable.setItem(row, 4, QtWidgets.QTableWidgetItem(", ".join(pwnedList["Breaches"][row]["DataClasses"])))
                    item = self.breachesTable.item(row, 4)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    self.breachesTable.setItem(row, 5, QtWidgets.QTableWidgetItem(pwnedList["Breaches"][row]["BreachDate"]))
                    item = self.breachesTable.item(row, 5)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    self.breachesTable.setItem(row, 6, QtWidgets.QTableWidgetItem(pwnedList["Breaches"][row]["Description"]))
                    item = self.breachesTable.item(row, 6)
                    item.setForeground(QBrush(QColor(248, 248, 242)))

                    row += 1

        
        if _ip != "" and self.previousIp != _ip:
            self.previousIp = _ip

            #Ip Lookup
            iplookupResoult = geoipLookup(_ip)

            lines = iplookupResoult.splitlines()

            self.hostname.setText(lines[1].split("Hostname:",1)[1])
            self.asn.setText(lines[2].split("ASN:",1)[1])
            self.organization.setText(lines[4].split("Organization:",1)[1])
            self.type.setText(lines[6].split("Type:",1)[1])
            self.assignment.setText(lines[7].split("Assignment:",1)[1])
            self.continent.setText(lines[8].split("Continent:",1)[1])
            self.country.setText(lines[9].split("Country:",1)[1])
            self.region.setText(lines[10].split("State/Region:",1)[1])
            self.city.setText(lines[11].split("City:",1)[1])
            self.latitude.setText(lines[12].split("Latitude:",1)[1])
            self.longitude.setText(lines[13].split("Longitude:",1)[1])
            self.postalcode.setText(lines[14].split("Postal Code:",1)[1])

            #check Torrent Downloads
            ikwdResoult = ikwd(_ip)

            row = 0
            self.downloads.setRowCount(len(ikwdResoult))
            for download in ikwdResoult:
                self.downloads.setItem(row, 0, QtWidgets.QTableWidgetItem(download[0]))
                item = self.downloads.item(row, 0)
                item.setForeground(QBrush(QColor(248, 248, 242)))               

                self.downloads.setItem(row, 1, QtWidgets.QTableWidgetItem(download[2]))
                item = self.downloads.item(row, 1)
                item.setForeground(QBrush(QColor(248, 248, 242)))

                self.downloads.setItem(row, 2, QtWidgets.QTableWidgetItem(download[3]))
                item = self.downloads.item(row, 2)
                item.setForeground(QBrush(QColor(248, 248, 242)))

                self.downloads.setItem(row, 3, QtWidgets.QTableWidgetItem(download[4]))
                item = self.downloads.item(row, 3)
                item.setForeground(QBrush(QColor(248, 248, 242)))

                row += 1

        if _nick != "" and self.previousNick != _nick:    
            self.previousNick = _nick

            #check accounts with target nickname
            whatsmynameList = whatsmyname(_nick)

            self.accountsNickname.clear()

            wtnIndex = 0
            for wtnAcc in whatsmynameList:
                self.accountsNickname.addItem(wtnAcc.replace('Found user at ', '', 1))
                acc = self.accountsNickname.item(wtnIndex)
                acc.setForeground(QBrush(QColor(248, 248, 242)))    
                wtnIndex += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
