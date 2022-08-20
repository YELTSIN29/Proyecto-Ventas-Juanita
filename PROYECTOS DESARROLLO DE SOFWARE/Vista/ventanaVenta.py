from PyQt5 import QtWidgets, uic
from Controlador.arregloRegCliente import ArregloVentas
from Controlador.registroCliente import RegistroCliente
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
            self.btnEnviarPedido.clicked.connect(self.listarRegPedido)
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
      def validaCliente(self):
            if self.txtDNI.text() == "":
                  self.txtDNI.setFocus()
                  return "DNI del cliente...!!!"
            elif self.txtNombre.text() == "":
                  self.txtNombre.setFocus()
                  return "Nombre del cliente...!!!"
            elif self.txtApellidoP.text() == "":
                  self.txtApellidoP.setFocus()
                  return "Apellido Paterno del cliente...!!!"
            elif self.txtApellidoM.text() == "":
                  self.txtApellidoM.setFocus()
                  return "Apellido Materno del cliente...!!!"
            elif self.txtCorreo.text() == "":
                  self.txtCorreo.setFocus()
                  return "Dirección del cliente...!!!"
            elif self.txtTelefono.text() == "":
                  self.txtTelefono.setFocus()
                  return "Teléfono del cliente...!!!"
            else:
                  return ""
      
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
      
      def validaPedido(self):
            if self.txtDNIcliente.text() == "":
                  self.txtDNIcliente.setFocus()
                  return "DNI del cliente...!!!"
            elif self.txtPrecioU.text() == "":
                  self.txtPrecioU.setFocus()
                  return "Precio del Producto...!!!"
            elif self.txtCantidad.text() == "":
                  self.txtCantidad.setFocus()
                  return "Cantidad del Producto...!!!"
            elif self.txtDescuento.text() == "":
                  self.txtDescuento.setFocus()
                  return "Descuento del producto...!!!"
            else:
                  return ""
      
      def registrarCliente(self):
            if self.validaCliente() == "":
                  objCli = RegistroCliente(self.obtenerDni(),
                                    self.obtenerNombre(), 
                                    self.obtenerApellidoP(), 
                                    self.obtenerApellidoM(), 
                                    self.obtenerCorreo(), 
                                    self.obtenerTelefono())
                  aCli.adicionaCliente(objCli)
                  aCli.grabarCliente()
                  self.limpiarControles()
            else:
                  QtWidgets.QMessageBox.information(self, "Registro del Cliente", 
                                     "Error en " + self.validaCliente(), QtWidgets.QMessageBox.Ok)
      def registrarpedido(self):
            if self.validaPedido() == "":
                  objPedido = RegPedido(self.obtenerPedidoDNI(), 
                                    self.obtenerPedidoProducto(), 
                                    self.obtenerPedidoDescripcion(), 
                                    self.obtenerPrecio(), 
                                    self.obtenerCantidad(), 
                                    self.obtenerDescuento())
                  aPedi.adicionaRegPedido(objPedido)
                  aPedi.grabarPedido()
                  self.limpiarControlesPedido()
                  self.listarRegPedido()
            else:
                  QtWidgets.QMessageBox.information(self, "Registro del Pedido", 
                                     "Error en " + self.validaPedido(), QtWidgets.QMessageBox.Ok)
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
            
      def listarRegPedido(self):
            self.tblListaPedido.setRowCount(aPedi.tamañoArregloRegPedido())
            self.tblListaPedido.setColumnCount(6)
            #Cabecera
            self.tblListaPedido.verticalHeader().setVisible(False)
            for i in range(0, aPedi.tamañoArregloRegPedido()):
                  self.tblListaPedido.setItem(i, 0, QtWidgets.QTableWidgetItem(aPedi.devolverRegPedido(i).getPedidoDNI()))
                  self.tblListaPedido.setItem(i, 1, QtWidgets.QTableWidgetItem(aPedi.devolverRegPedido(i).getPedidoProducto()))
                  self.tblListaPedido.setItem(i, 2, QtWidgets.QTableWidgetItem(aPedi.devolverRegPedido(i).getPedidoDescripcion()))
                  self.tblListaPedido.setItem(i, 3, QtWidgets.QTableWidgetItem(aPedi.devolverRegPedido(i).getCantidad()))
                  self.tblListaPedido.setItem(i, 4, QtWidgets.QTableWidgetItem(aPedi.devolverRegPedido(i).getPrecio()))
                  self.tblListaPedido.setItem(i, 5, QtWidgets.QTableWidgetItem(aPedi.devolverRegPedido(i).getDescuento()))
