# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yelts\OneDrive\Escritorio\Proyecto Ventas Juanita\PROYECTOS DESARROLLO DE SOFWARE\Formulario\admi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\Proyecto Ventas Juanita\\PROYECTOS DESARROLLO DE SOFWARE\\Formulario\\logo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.btnSalidaAdmi = QtWidgets.QPushButton(self.menubotones)
        self.btnSalidaAdmi.setGeometry(QtCore.QRect(20, 660, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnSalidaAdmi.setFont(font)
        self.btnSalidaAdmi.setObjectName("btnSalidaAdmi")
        self.verticalLayout_2.addWidget(self.menubotones)
        self.horizontalLayout_2.addWidget(self.menuizquierdo)
        self.menuderecho = QtWidgets.QFrame(self.frame_2)
        self.menuderecho.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menuderecho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuderecho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuderecho.setObjectName("menuderecho")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menuderecho)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.paginas = QtWidgets.QStackedWidget(self.menuderecho)
        font = QtGui.QFont()
        font.setKerning(True)
        self.paginas.setFont(font)
        self.paginas.setStyleSheet("")
        self.paginas.setObjectName("paginas")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(80, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(80, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(80, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(80, 320, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtNombreTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtNombreTrabajo.setGeometry(QtCore.QRect(270, 170, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtNombreTrabajo.setFont(font)
        self.txtNombreTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtNombreTrabajo.setObjectName("txtNombreTrabajo")
        self.txtApellidoPTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtApellidoPTrabajo.setGeometry(QtCore.QRect(270, 240, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtApellidoPTrabajo.setFont(font)
        self.txtApellidoPTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtApellidoPTrabajo.setObjectName("txtApellidoPTrabajo")
        self.txtApellidoMTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtApellidoMTrabajo.setGeometry(QtCore.QRect(270, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtApellidoMTrabajo.setFont(font)
        self.txtApellidoMTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtApellidoMTrabajo.setObjectName("txtApellidoMTrabajo")
        self.txtDNITrabajo = QtWidgets.QLineEdit(self.page)
        self.txtDNITrabajo.setGeometry(QtCore.QRect(270, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtDNITrabajo.setFont(font)
        self.txtDNITrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtDNITrabajo.setObjectName("txtDNITrabajo")
        self.txtTelefonoTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtTelefonoTrabajo.setGeometry(QtCore.QRect(270, 390, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtTelefonoTrabajo.setFont(font)
        self.txtTelefonoTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtTelefonoTrabajo.setObjectName("txtTelefonoTrabajo")
        self.label_25 = QtWidgets.QLabel(self.page)
        self.label_25.setGeometry(QtCore.QRect(70, 0, 621, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.txtCorreoTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtCorreoTrabajo.setGeometry(QtCore.QRect(270, 460, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtCorreoTrabajo.setFont(font)
        self.txtCorreoTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtCorreoTrabajo.setText("")
        self.txtCorreoTrabajo.setObjectName("txtCorreoTrabajo")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(80, 460, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(80, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtCargoTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtCargoTrabajo.setGeometry(QtCore.QRect(270, 530, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtCargoTrabajo.setFont(font)
        self.txtCargoTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtCargoTrabajo.setText("")
        self.txtCargoTrabajo.setObjectName("txtCargoTrabajo")
        self.btnRegistroTrabajo = QtWidgets.QPushButton(self.page)
        self.btnRegistroTrabajo.setGeometry(QtCore.QRect(340, 690, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.btnRegistroTrabajo.setFont(font)
        self.btnRegistroTrabajo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistroTrabajo.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.06, y2:0.131227, stop:0.373134 rgba(249, 148, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.btnRegistroTrabajo.setObjectName("btnRegistroTrabajo")
        self.txtSueldoTrabajo = QtWidgets.QLineEdit(self.page)
        self.txtSueldoTrabajo.setGeometry(QtCore.QRect(270, 600, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtSueldoTrabajo.setFont(font)
        self.txtSueldoTrabajo.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 0, 127);\n"
"padding-bottom:7px;\n"
"}")
        self.txtSueldoTrabajo.setText("")
        self.txtSueldoTrabajo.setObjectName("txtSueldoTrabajo")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(80, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.paginas.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(290, 270, 291, 261))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\Proyecto Ventas Juanita\\PROYECTOS DESARROLLO DE SOFWARE\\Formulario\\logoSinFondo2.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.tblListaTrabajo = QtWidgets.QTableWidget(self.page_2)
        self.tblListaTrabajo.setGeometry(QtCore.QRect(30, 140, 831, 421))
        self.tblListaTrabajo.setStyleSheet("border:2px solid rgb(255, 85, 127);")
        self.tblListaTrabajo.setObjectName("tblListaTrabajo")
        self.tblListaTrabajo.setColumnCount(8)
        self.tblListaTrabajo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaTrabajo.setHorizontalHeaderItem(7, item)
        self.label_27 = QtWidgets.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(210, 20, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.btnConsultaTrabajador = QtWidgets.QPushButton(self.page_2)
        self.btnConsultaTrabajador.setGeometry(QtCore.QRect(330, 620, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.btnConsultaTrabajador.setFont(font)
        self.btnConsultaTrabajador.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConsultaTrabajador.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.06, y2:0.131227, stop:0.373134 rgba(249, 148, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.btnConsultaTrabajador.setObjectName("btnConsultaTrabajador")
        self.paginas.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("")
        self.page_3.setObjectName("page_3")
        self.label_28 = QtWidgets.QLabel(self.page_3)
        self.label_28.setGeometry(QtCore.QRect(200, 20, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.tblListaCliente = QtWidgets.QTableWidget(self.page_3)
        self.tblListaCliente.setGeometry(QtCore.QRect(70, 140, 761, 431))
        self.tblListaCliente.setStyleSheet("border:2px solid rgb(255, 85, 127);")
        self.tblListaCliente.setObjectName("tblListaCliente")
        self.tblListaCliente.setColumnCount(6)
        self.tblListaCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblListaCliente.setHorizontalHeaderItem(5, item)
        self.btnConsultaCliente = QtWidgets.QPushButton(self.page_3)
        self.btnConsultaCliente.setGeometry(QtCore.QRect(340, 640, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.btnConsultaCliente.setFont(font)
        self.btnConsultaCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConsultaCliente.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.06, y2:0.131227, stop:0.373134 rgba(249, 148, 207, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.btnConsultaCliente.setObjectName("btnConsultaCliente")
        self.paginas.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setStyleSheet("")
        self.page_4.setObjectName("page_4")
        self.paginas.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setStyleSheet("")
        self.page_5.setObjectName("page_5")
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
        self.label_23.setPixmap(QtGui.QPixmap("c:\\Users\\yelts\\OneDrive\\Escritorio\\Proyecto Ventas Juanita\\PROYECTOS DESARROLLO DE SOFWARE\\Formulario\\logo1.png"))
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
        self.btnPag2.setText(_translate("MainWindow", "Trabajadores"))
        self.btnPag3.setText(_translate("MainWindow", "Lista Cliente"))
        self.btnPag4.setText(_translate("MainWindow", "pag4"))
        self.btnPag5.setText(_translate("MainWindow", "pag5"))
        self.btnSalir.setText(_translate("MainWindow", "salir"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff007f;\">Ropa Juanita</span></p></body></html>"))
        self.btnSalidaAdmi.setText(_translate("MainWindow", "Salir"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_3.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.label_4.setText(_translate("MainWindow", "DNI:"))
        self.label_5.setText(_translate("MainWindow", "Telefono:"))
        self.label_6.setText(_translate("MainWindow", "Apellido Materno:"))
        self.label_25.setText(_translate("MainWindow", "Registro del Trabajador"))
        self.label_7.setText(_translate("MainWindow", "Correo:"))
        self.label_9.setText(_translate("MainWindow", "Cargo:"))
        self.btnRegistroTrabajo.setText(_translate("MainWindow", "Registrar"))
        self.label_10.setText(_translate("MainWindow", "Sueldo:"))
        item = self.tblListaTrabajo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tblListaTrabajo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.tblListaTrabajo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "APELLIDO P"))
        item = self.tblListaTrabajo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "APELLIDO M"))
        item = self.tblListaTrabajo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TELEFONO"))
        item = self.tblListaTrabajo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CORREO"))
        item = self.tblListaTrabajo.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CARGO"))
        item = self.tblListaTrabajo.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "SUELDO"))
        self.label_27.setText(_translate("MainWindow", "Lista de Trabajadores"))
        self.btnConsultaTrabajador.setText(_translate("MainWindow", "Consultar"))
        self.label_28.setText(_translate("MainWindow", "Lista de Clientes"))
        item = self.tblListaCliente.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tblListaCliente.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.tblListaCliente.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "APELLIDO P"))
        item = self.tblListaCliente.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "APELLIDO M"))
        item = self.tblListaCliente.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TELEFONO"))
        item = self.tblListaCliente.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CORREO"))
        self.btnConsultaCliente.setText(_translate("MainWindow", "Consultar"))
        self.label_21.setText(_translate("MainWindow", "BIENVENIDO "))
        self.label_22.setText(_translate("MainWindow", "VENTANA DEL ADMINISTRADOR"))
