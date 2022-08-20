from PyQt5 import QtWidgets, uic
from Controlador.registroProducto import RegProducto
from Controlador.arregloRegProducto import ArregloRegProducto

argpro=ArregloRegProducto()

class VentanaAlmacen(QtWidgets.QMainWindow):
      def __init__(self,parent = None):
            super(VentanaAlmacen,self).__init__(parent)
            uic.loadUi("Formulario/Almacen.ui",self)
            self.btnRegProducto.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
            self.btnListaProductos.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_3))
            self.setFixedWidth(956)
            self.setFixedHeight(714) 
            self.btnSalir.clicked.connect(self.Salir)
            self.btnAgregarProducto.clicked.connect(self.registrarProducto)
            self.btnConsultaProducto.clicked.connect(self.listarRegProducto)
      
      def Salir(self):
            self.close()
            
      def obtenerCodProducto(self):
            return self.txtRegCodProducto.text()
      
      def obtenerCategoriaProducto(self):
            return self.cbxRegCatgProducto.currentText()
      
      def obtenerDescripcionProducto(self):
            return self.txtRegDescripcion.text()
      
      def obtenerTallaProducto(self):
            return self.txtRegTalla.text()
      
      def obtenerMarcaProducto(self):
            return self.txtRegMarca.text()
      
      def obtenerCantidadProducto(self):
            return self.txtRegCantidad.text()
      
      def obtenerPrecioProducto(self):
            return self.txtRegPrecioUni.text()
      
      def registrarProducto(self):
            if self.validaRegProducto() == "":
                  objProducto = RegProducto(self.obtenerCodProducto(),
                              self.obtenerCategoriaProducto(),
                              self.obtenerDescripcionProducto(),
                              self.obtenerTallaProducto(),
                              self.obtenerMarcaProducto(),
                              self.obtenerCantidadProducto(),
                              self.obtenerPrecioProducto())
                  argpro.adicionaRegProducto(objProducto)
                  argpro.grabarProducto()
                  self.limpiarControles()
                  self.listarRegProducto()
            else:
                  QtWidgets.QMessageBox.information(self, "Registrar Producto", 
                                     "Error en " + self.validaRegProducto(), QtWidgets.QMessageBox.Ok)
      def limpiarControles(self):
            self.txtRegCodProducto.clear()
            self.txtRegDescripcion.clear()
            self.txtRegTalla.clear()
            self.txtRegMarca.clear()
            self.txtRegCantidad.clear()
            self.txtRegPrecioUni.clear()
            
      def listarRegProducto(self):
            self.tblListaProducto.setRowCount(argpro.tamañoArregloRegProducto())
            self.tblListaProducto.setColumnCount(6)
            #Cabecera
            self.tblListaProducto.verticalHeader().setVisible(False)
            for i in range(0, argpro.tamañoArregloRegProducto()):
                  self.tblListaProducto.setItem(i, 0, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getCodProducto()))
                  self.tblListaProducto.setItem(i, 1, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getCategoria()))
                  self.tblListaProducto.setItem(i, 2, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getDecripcion()))
                  self.tblListaProducto.setItem(i, 3, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getTalla()))
                  self.tblListaProducto.setItem(i, 4, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getMarca()))
                  self.tblListaProducto.setItem(i, 5, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getCantidad()))
                  self.tblListaProducto.setItem(i, 6, QtWidgets.QTableWidgetItem(argpro.devolverRegProducto(i).getPrecio()))
      
      def validaRegProducto(self):
            if self.txtRegCodProducto.text() == "":
                  self.txtRegCodProducto.setFocus()
                  return "Codigo del Producto...!!!"
            elif self.txtRegDescripcion.text() == "":
                  self.txtRegDescripcion.setFocus()
                  return "Descripcion del Producto...!!!"
            elif self.txtRegTalla.text() == "":
                  self.txtRegTalla.setFocus()
                  return "Talla del Producto...!!!"
            elif self.txtRegMarca.text() == "":
                  self.txtRegMarca.setFocus()
                  return "Marca del producto...!!!"
            elif self.txtRegCantidad.text() == "":
                  self.txtRegCantidad.setFocus()
                  return "Cantidad del producto...!!!"
            elif self.txtRegPrecioUni.text() == "":
                  self.txtRegPrecioUni.setFocus()
                  return "Precio del Producto...!!!"
            else:
                  return ""