from PyQt5 import QtWidgets, uic

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
      def Salir(self):
            self.close()