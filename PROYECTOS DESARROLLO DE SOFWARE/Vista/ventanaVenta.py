from PyQt5 import QtWidgets, uic
from Controlador.arregloRegCliente import ArregloVentas
from Controlador.registroCliente import Registro
#from Controlador.arregloRegProducto import ArregloRegProducto
from Controlador.registroPedido import RegPedido
#from Controlador.registroProducto import RegProducto
from Controlador.arregloRegistroPedido import ArregloRegPedido

aCli = ArregloVentas()
aPedi= ArregloRegPedido()
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
            self.btnGuardarRgtr.clicked.connect(self.registrarCliente)
            self.btnAgregarPedido.clicked.connect(self.registrarpedido)
            self.btnLimpiarPedido.clicked.connect(self.limpiarControlesPedido)
      def Salir(self):
            self.close()
      #obtener registro del cliente      
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
      
      #obtener registro del pedido
      def obtenerPedidoDNI(self):
            return self.txtDNIcliente.text()
      
      def obtenerPedidoProducto(self):
            return self.cbxProducto.currentText()
      
      def obtenerPedidoDescripcion(self):
            return self.cbxPrenda.currentText()
      
      def obtenerPrecio(self):
            return self.txtPrecioU.text()
      
      def obtenerCantidad(self):
            return self.txtCantidad.text()
      
      def obtenerDescuento(self):
            return self.txtDescuento.text()
      
      def registrarCliente(self):
            objCli = Registro(self.obtenerDni(),
                              self.obtenerNombre(), 
                              self.obtenerApellidoP(), 
                              self.obtenerApellidoM(), 
                              self.obtenerCorreo(), 
                              self.obtenerTelefono())
            aCli.adicionaCliente(objCli)
            aCli.grabarCliente()
            self.limpiarControles()
      
      def registrarpedido(self):
            objPedido = RegPedido(self.obtenerPedidoDNI(), 
                              self.obtenerPedidoProducto(), 
                              self.obtenerPedidoDescripcion(), 
                              self.obtenerPrecio(), 
                              self.obtenerCantidad(), 
                              self.obtenerDescuento())
            aPedi.adicionaRegPedido(objPedido)
            aPedi.grabarPedido()
            self.limpiarControles()
            
      def limpiarControles(self):
            self.txtDNI.clear()
            self.txtNombre.clear()
            self.txtApellidoP.clear()
            self.txtApellidoM.clear()
            self.txtCorreo.clear()
            self.txtTelefono.clear()
      
      def limpiarControlesPedido(self):
            self.txtDNIcliente.clear()
            self.txtPrecioU.clear()
            self.txtCantidad.clear()
            self.txtDescuento.clear()
            self.txtCorreo.clear()
            self.txtTelefono.clear()
            
