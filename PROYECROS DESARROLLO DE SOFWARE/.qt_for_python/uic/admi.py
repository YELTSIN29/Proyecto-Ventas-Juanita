# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yelts\OneDrive\Escritorio\PROYECROS DESARROLLO DE SOFWARE\Formulario\admi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 714)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuizquierdo = QtWidgets.QFrame(self.frame_2)
        self.menuizquierdo.setMinimumSize(QtCore.QSize(180, 0))
        self.menuizquierdo.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menuizquierdo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuizquierdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuizquierdo.setObjectName("menuizquierdo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menuizquierdo)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menubotones = QtWidgets.QFrame(self.menuizquierdo)
        self.menubotones.setStyleSheet("QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.06, y2:0.131227, stop:0.373134 rgba(249, 148, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QPushButton{\n"
"border:2px solid rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}")
        self.menubotones.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menubotones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menubotones.setObjectName("menubotones")
        self.btnRegistro = QtWidgets.QPushButton(self.menubotones)
        self.btnRegistro.setGeometry(QtCore.QRect(30, 110, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnRegistro.setFont(font)
        self.btnRegistro.setObjectName("btnRegistro")
        self.btnPag2 = QtWidgets.QPushButton(self.menubotones)
        self.btnPag2.setGeometry(QtCore.QRect(30, 190, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnPag2.setFont(font)
        self.btnPag2.setObjectName("btnPag2")
        self.btnPag3 = QtWidgets.QPushButton(self.menubotones)
        self.btnPag3.setGeometry(QtCore.QRect(30, 280, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnPag3.setFont(font)
        self.btnPag3.setObjectName("btnPag3")
        self.btnPag4 = QtWidgets.QPushButton(self.menubotones)
        self.btnPag4.setGeometry(QtCore.QRect(30, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnPag4.setFont(font)
        self.btnPag4.setObjectName("btnPag4")
        self.btnPag5 = QtWidgets.QPushButton(self.menubotones)
        self.btnPag5.setGeometry(QtCore.QRect(30, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnPag5.setFont(font)
        self.btnPag5.setObjectName("btnPag5")
        self.btnSalir = QtWidgets.QPushButton(self.menubotones)
        self.btnSalir.setGeometry(QtCore.QRect(30, 790, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.label_24 = QtWidgets.QLabel(self.menubotones)
        self.label_24.setGeometry(QtCore.QRect(0, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.menubotones)
        self.horizontalLayout_2.addWidget(self.menuizquierdo)
        self.menuderecho = QtWidgets.QFrame(self.frame_2)
        self.menuderecho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuderecho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuderecho.setObjectName("menuderecho")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menuderecho)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.paginas = QtWidgets.QStackedWidget(self.menuderecho)
        self.paginas.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.paginas.setObjectName("paginas")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(270, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(80, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(80, 260, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(80, 420, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(80, 500, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(80, 340, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 260, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 340, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_6.setGeometry(QtCore.QRect(270, 500, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 710, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 710, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.page)
        self.pushButton_10.setGeometry(QtCore.QRect(720, 710, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.paginas.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(290, 270, 291, 261))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\PROYECROS DESARROLLO DE SOFWARE\\Formulario\\logoSinFondo2.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 290, 161, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(240, 200, 161, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(90, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(90, 290, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(90, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(240, 110, 161, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.paginas.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_3.setObjectName("page_3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(700, 50, 161, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(550, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(550, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(550, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(700, 230, 161, 41))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(700, 140, 161, 41))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.paginas.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.page_4.setObjectName("page_4")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(240, 550, 161, 41))
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setGeometry(QtCore.QRect(90, 730, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setGeometry(QtCore.QRect(90, 650, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(90, 550, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(240, 730, 161, 41))
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(240, 640, 161, 41))
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.paginas.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(38, 160, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.page_5.setObjectName("page_5")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(260, 70, 161, 41))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_17 = QtWidgets.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(110, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_5)
        self.label_18.setGeometry(QtCore.QRect(110, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_5)
        self.label_19.setGeometry(QtCore.QRect(110, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(260, 250, 161, 41))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(260, 160, 161, 41))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.paginas.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.page_6.setObjectName("page_6")
        self.label_21 = QtWidgets.QLabel(self.page_6)
        self.label_21.setGeometry(QtCore.QRect(150, 30, 511, 121))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(48)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_6)
        self.label_22.setGeometry(QtCore.QRect(80, 210, 621, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.page_6)
        self.label_23.setGeometry(QtCore.QRect(220, 340, 331, 341))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\PROYECROS DESARROLLO DE SOFWARE\\Formulario\\logo1.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.paginas.addWidget(self.page_6)
        self.verticalLayout_3.addWidget(self.paginas)
        self.horizontalLayout_2.addWidget(self.menuderecho)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.paginas.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VENTANA DEL ADMINISTRADOR"))
        self.btnRegistro.setText(_translate("MainWindow", "Registrar"))
        self.btnPag2.setText(_translate("MainWindow", "pedido"))
        self.btnPag3.setText(_translate("MainWindow", "pag3"))
        self.btnPag4.setText(_translate("MainWindow", "pag4"))
        self.btnPag5.setText(_translate("MainWindow", "pag5"))
        self.btnSalir.setText(_translate("MainWindow", "salir"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff007f;\">Ropa Juanita</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Codigo:"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_3.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.label_4.setText(_translate("MainWindow", "DNI:"))
        self.label_5.setText(_translate("MainWindow", "Telefono:"))
        self.label_6.setText(_translate("MainWindow", "Apellido Materno:"))
        self.pushButton_7.setText(_translate("MainWindow", "guardar"))
        self.pushButton_8.setText(_translate("MainWindow", "modificar"))
        self.pushButton_10.setText(_translate("MainWindow", "guardar"))
        self.label_9.setText(_translate("MainWindow", "producto"))
        self.label_10.setText(_translate("MainWindow", "Apellido"))
        self.label_20.setText(_translate("MainWindow", "cod_pedido"))
        self.label_11.setText(_translate("MainWindow", "Apellido"))
        self.label_12.setText(_translate("MainWindow", "nombre"))
        self.label_13.setText(_translate("MainWindow", "cod_cliente"))
        self.label_14.setText(_translate("MainWindow", "Apellido"))
        self.label_15.setText(_translate("MainWindow", "nombre"))
        self.label_16.setText(_translate("MainWindow", "cod_cliente"))
        self.label_17.setText(_translate("MainWindow", "Apellido"))
        self.label_18.setText(_translate("MainWindow", "nombre"))
        self.label_19.setText(_translate("MainWindow", "cod_cliente"))
        self.label_21.setText(_translate("MainWindow", "BIENVENIDO "))
        self.label_22.setText(_translate("MainWindow", "VENTANA DEL ADMINISTRADOR"))
