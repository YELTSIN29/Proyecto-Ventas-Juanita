from PyQt5 import QtWidgets, uic
from Controlador.registroProducto import RegProducto
from Controlador.arregloRegProducto import ArregloRegProducto

argpro=ArregloRegProducto()

class VentanaAlmacen(QtWidgets.QMainWindow):
      def __init__(self,parent = None):
            super(VentanaAlmacen,self).__init__(parent)
            uic.loadUi("Formulario/Almacen.ui",self)
            self.btnpag.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page))
            self.btnRegProducto.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
            self.btnPag3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_3))
            self.btnPag4.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
            self.btnPag5.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_5))
            self.setFixedWidth(956)
            self.setFixedHeight(714) 
            self.btnSalir.clicked.connect(self.Salir)
            self.btnAgregarProducto.clicked.connect(self.registrar)
      
      def Salir(self):
            self.close()
            
      def obtenerCodProducto(self):
            return self.txtRegCodProducto.text()
      
      def obtenerCategoriaProducto(self):
            return self.cbxRegCatgProducto.currentText()
      
      def obtenerDescripcionProducto(self):
            return self.txtRegDescripcion.text()
      
      def obtenerCantidadProducto(self):
            return self.txtRegCantidad.text()
      
      def obtenerPrecioProducto(self):
            return self.txtRegPrecioUni.text()
      
      def registrar(self):
            objProducto = RegProducto(self.obtenerCodProducto(),
                        self.obtenerCategoriaProducto(),
                        self.obtenerDescripcionProducto(),
                        self.obtenerCantidadProducto(),
                        self.obtenerPrecioProducto())
            argpro.adicionaRegProducto(objProducto)
            argpro.grabarProducto()
            self.limpiarControles()
            
      def limpiarControles(self):
            self.txtRegCodProducto.clear()
            self.txtRegDescripcion.clear()
            self.txtRegCantidad.clear()
            self.txtRegPrecioUni.clear()
            