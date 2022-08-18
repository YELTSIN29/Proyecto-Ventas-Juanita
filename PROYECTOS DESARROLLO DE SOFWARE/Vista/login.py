from PyQt5 import QtWidgets, uic

from Vista.ventanaAdmi import VentanaAdmi
from Vista.ventanaCaja import VentanaCaja
from Vista.ventanaAlmacen import VentanaAlmacen
from Vista.ventanaVenta import VentanaVenta


class Login(QtWidgets.QMainWindow):
      def __init__(self,parent = None):
            super(Login,self).__init__(parent)
            uic.loadUi("Formulario/LoginJuanita.ui",self)
            self.show()
            self.setFixedWidth(421)
            self.setFixedHeight(654)
            self.btnIngresar.clicked.connect(self.iniciarSesion)
      def iniciarSesion(self):
            usuario = self.cbxUsuario.currentText()
            contraseña = self.txtPassword.text()
            if usuario == "[Usuario]":
                  self.lblError2.setText(str("Elija un Usuario"))    
            elif usuario == "Administrador" and contraseña == "1111":
                  #self.close()
                  vprincipal = VentanaAdmi(self)
                  vprincipal.show()
                  self.Limpiar()
            elif usuario == "Cajero" and contraseña == "2222":
                  #self.close()
                  vprincipal = VentanaCaja(self)
                  vprincipal.show()
                  self.Limpiar()
            elif usuario == "Almacen" and contraseña == "3333":
                  #self.close()
                  vprincipal = VentanaAlmacen(self)
                  vprincipal.show()
                  self.Limpiar()
            elif usuario == "Venta" and contraseña == "4444":
                  #self.close()
                  vprincipal = VentanaVenta(self)
                  vprincipal.show()
                  self.Limpiar()
            else:
                  self.lblError.setText(str("Contraseña Incorrecta"))
                  self.Limpiar()   
                        
      def Limpiar(self):
            self.txtPassword.setText("")
            
            
            