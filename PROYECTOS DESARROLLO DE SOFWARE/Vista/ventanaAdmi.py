from PyQt5 import QtWidgets, uic
from Controlador.arregloRegCliente import *
from Vista.ventanaVenta import *
from Controlador.arregloRegTrabajador import *

aTrab=ArregloTrabajador()

class VentanaAdmi(QtWidgets.QMainWindow):
      def __init__(self,parent = None):
            super(VentanaAdmi,self).__init__(parent)
            uic.loadUi("Formulario/admi.ui",self)
            self.btnRegistro.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page))
            self.btnPag2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
            self.btnPag3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_3))
            self.btnPag4.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
            self.btnPag5.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_5))
            self.setFixedWidth(1060)
            self.setFixedHeight(760) 
            self.btnSalidaAdmi.clicked.connect(self.Salir)
            self.btnConsultaCliente.clicked.connect(self.listarRegCliente)
            self.btnRegistroTrabajo.clicked.connect(self.registrarTrabajador)
            self.btnConsultaTrabajador.clicked.connect(self.listarTrabajador)
      def Salir(self):
            self.close()
      
      #obtener registro del Trabajador    
      def obtenerDniTrab(self):
            return self.txtDNITrabajo.text()
      
      def obtenerNombreTrab(self):
            return self.txtNombreTrabajo.text()
      
      def obtenerApellidoPTrab(self):
            return self.txtApellidoPTrabajo.text()
      
      def obtenerApellidoMTrab(self):
            return self.txtApellidoMTrabajo.text()
      
      def obtenerCorreoTrab(self):
            return self.txtCorreoTrabajo.text()
      
      def obtenerTelefonoTrab(self):
            return self.txtTelefonoTrabajo.text()
      
      def obtenerCargoTrab(self):
            return self.txtCargoTrabajo.text()
      
      def obtenerSueldoTrab(self):
            return self.txtSueldoTrabajo.text()
      
      def registrarTrabajador(self):
            if self.validaTrabajador() == "":
                  objtrabajador = RegistroTrabajador(self.obtenerDniTrab(),
                                    self.obtenerNombreTrab(), 
                                    self.obtenerApellidoPTrab(), 
                                    self.obtenerApellidoMTrab(), 
                                    self.obtenerCorreoTrab(), 
                                    self.obtenerTelefonoTrab(),
                                    self.obtenerCargoTrab(),
                                    self.obtenerSueldoTrab())
                  aTrab.adicionaTrabajador(objtrabajador)
                  aTrab.grabarTrabajador()
                  self.limpiarControles()
                  self.listarTrabajador()
            else:
                  QtWidgets.QMessageBox.information(self, "Registrar Trabajador", 
                                     "Error en " + self.validaTrabajador(), QtWidgets.QMessageBox.Ok)
            
      def limpiarControles(self):
            self.txtDNITrabajo.clear()
            self.txtNombreTrabajo.clear()
            self.txtApellidoPTrabajo.clear()
            self.txtApellidoMTrabajo.clear()
            self.txtCorreoTrabajo.clear()
            self.txtTelefonoTrabajo.clear()
            self.txtCargoTrabajo.clear()
            self.txtSueldoTrabajo.clear()
            
      def listarTrabajador(self):
            self.tblListaTrabajo.setRowCount(aTrab.tamañoArregloTrabajador())
            self.tblListaTrabajo.setColumnCount(8)
            #Cabecera
            self.tblListaTrabajo.verticalHeader().setVisible(False)
            for i in range(0, aTrab.tamañoArregloTrabajador()):
                  self.tblListaTrabajo.setItem(i, 0, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabDNI()))
                  self.tblListaTrabajo.setItem(i, 1, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabNombre()))
                  self.tblListaTrabajo.setItem(i, 2, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabApellidoP()))
                  self.tblListaTrabajo.setItem(i, 3, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabApellidoM()))
                  self.tblListaTrabajo.setItem(i, 4, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabTelefono()))
                  self.tblListaTrabajo.setItem(i, 5, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabCorreo()))
                  self.tblListaTrabajo.setItem(i, 6, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabCargo()))
                  self.tblListaTrabajo.setItem(i, 7, QtWidgets.QTableWidgetItem(aTrab.devolverTrabajador(i).getRegistroTrabSueldo()))
            
      def listarRegCliente(self):
            self.tblListaCliente.setRowCount(aCli.tamañoArregloCliente())
            self.tblListaCliente.setColumnCount(6)
            #Cabecera
            self.tblListaCliente.verticalHeader().setVisible(False)
            for i in range(0, aCli.tamañoArregloCliente()):
                  self.tblListaCliente.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getRegistroDNI()))
                  self.tblListaCliente.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getRegistroNombre()))
                  self.tblListaCliente.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getRegistroApellidoP()))
                  self.tblListaCliente.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getRegistroApellidoM()))
                  self.tblListaCliente.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getRegistroTelefono()))
                  self.tblListaCliente.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getRegistroCorreo()))
                  
      def validaTrabajador(self):
            if self.txtDNITrabajo.text() == "":
                  self.txtDNITrabajo.setFocus()
                  return "DNI del Trabajador...!!!"
            elif self.txtNombreTrabajo.text() == "":
                  self.txtNombreTrabajo.setFocus()
                  return "Nombre del Trabajador...!!!"
            elif self.txtApellidoPTrabajo.text() == "":
                  self.txtApellidoPTrabajo.setFocus()
                  return "Apellido Paterno del Trabajador...!!!"
            elif self.txtApellidoMTrabajo.text() == "":
                  self.txtApellidoMTrabajo.setFocus()
                  return "Apellido Materno del Trabajador...!!!"
            elif self.txtTelefonoTrabajo.text() == "":
                  self.txtTelefonoTrabajo.setFocus()
                  return "Telefono del Trabajador...!!!"
            elif self.txtCorreoTrabajo.text() == "":
                  self.txtCorreoTrabajo.setFocus()
                  return "Correo del Trabajador...!!!"
            elif self.txtCargoTrabajo.text() == "":
                  self.txtCargoTrabajo.setFocus()
                  return "Cargo del Trabajador...!!!"
            elif self.txtSueldoTrabajo.text() == "":
                  self.txtSueldoTrabajo.setFocus()
                  return "Sueldo del Trabajador...!!!"
            else:
                  return ""