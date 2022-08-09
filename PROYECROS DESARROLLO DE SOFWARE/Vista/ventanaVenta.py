from PyQt5 import QtWidgets, uic
from Controlador.arregloVentas import ArregloVentas
from Controlador.registroCliente import Registro
aCli = ArregloVentas()
class VentanaVenta(QtWidgets.QMainWindow):
      def __init__(self,parent = None):
            super(VentanaVenta,self).__init__(parent)
            uic.loadUi("Formulario/venta.ui",self)
            self.btnRegistro.clicked.connect(lambda: self.MenuPaginas.setCurrentWidget(self.pagRegistroCliente))
            self.btnPedido.clicked.connect(lambda: self.MenuPaginas.setCurrentWidget(self.pagPedidoCliente))
            self.btnLista.clicked.connect(lambda: self.MenuPaginas.setCurrentWidget(self.pagListaPedidos))
            self.btnConsulta.clicked.connect(lambda: self.MenuPaginas.setCurrentWidget(self.pagConsultaPedidos))
            self.btnCambio.clicked.connect(lambda: self.MenuPaginas.setCurrentWidget(self.pagCambio))
            self.setFixedWidth(956)
            self.setFixedHeight(714) 
            self.btnSalir.clicked.connect(self.Salir)
            self.btnGuardarRgtr.clicked.connect(self.registrar)
      def Salir(self):
            self.close()
            
      def obtenerDni(self):
            return self.txtDNI.text()
      
      def obtenerNombre(self):
            return self.txtNombre.text()
      
      def obtenerApellidoP(self):
            return self.txtApellidoP.text()
      
      def obtenerApellidoM(self):
            return self.txtApellidoM.text()
      
      def obtenerCorreo(self):
            return self.txtCorreo.text()
      
      def obtenerTelefono(self):
            return self.txtTelefono.text()
      def registrar(self):
            objCli = Registro(self.obtenerDni(), self.obtenerNombre(), 
                              self.obtenerApellidoP(), 
                              self.obtenerApellidoM(), 
                              self.obtenerCorreo(), self.obtenerTelefono())
            aCli.adicionaCliente(objCli)
            aCli.grabar()
            self.limpiarControles()
            
      def limpiarControles(self):
            self.txtDNI.clear()
            self.txtNombre.clear()
            self.txtApellidoP.clear()
            self.txtApellidoM.clear()
            self.txtCorreo.clear()
            self.txtTelefono.clear()