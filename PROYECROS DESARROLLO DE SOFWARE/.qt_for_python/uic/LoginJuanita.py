# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yelts\OneDrive\Escritorio\PROYECROS DESARROLLO DE SOFWARE\Formulario\LoginJuanita.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 654)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\PROYECROS DESARROLLO DE SOFWARE\\Formulario\\logo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 421, 671))
        self.label.setStyleSheet("border:3px solidrgb(255, 85, 127);\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.06, y2:0.131227, stop:0.373134 rgba(249, 148, 207, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 141, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\PROYECROS DESARROLLO DE SOFWARE\\Formulario\\logo1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIngresar.setGeometry(QtCore.QRect(130, 490, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    border-radius:20px;\n"
"    border:2px solid rgb(255, 0, 127);\n"
"    background-color:qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.713, fx:0.5, fy:0.5, stop:0.159204 rgba(228, 76, 147, 255), stop:0.890547 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnIngresar.setObjectName("btnIngresar")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(120, 380, 181, 41))
        self.txtPassword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtPassword.setObjectName("txtPassword")
        self.cbxUsuario = QtWidgets.QComboBox(self.centralwidget)
        self.cbxUsuario.setGeometry(QtCore.QRect(120, 300, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.cbxUsuario.setFont(font)
        self.cbxUsuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbxUsuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 0, 127)")
        self.cbxUsuario.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cbxUsuario.setObjectName("cbxUsuario")
        self.cbxUsuario.addItem("")
        self.cbxUsuario.addItem("")
        self.cbxUsuario.addItem("")
        self.cbxUsuario.addItem("")
        self.cbxUsuario.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lblError = QtWidgets.QLabel(self.centralwidget)
        self.lblError.setGeometry(QtCore.QRect(120, 430, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblError.setFont(font)
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")
        self.lblError2 = QtWidgets.QLabel(self.centralwidget)
        self.lblError2.setGeometry(QtCore.QRect(120, 350, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblError2.setFont(font)
        self.lblError2.setText("")
        self.lblError2.setObjectName("lblError2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cbxUsuario.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.cbxUsuario.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.cbxUsuario.setItemText(0, _translate("MainWindow", "[Usuario]"))
        self.cbxUsuario.setItemText(1, _translate("MainWindow", "Administrador"))
        self.cbxUsuario.setItemText(2, _translate("MainWindow", "Cajero"))
        self.cbxUsuario.setItemText(3, _translate("MainWindow", "Almacen"))
        self.cbxUsuario.setItemText(4, _translate("MainWindow", "Venta"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Bienvenido</span></p></body></html>"))
