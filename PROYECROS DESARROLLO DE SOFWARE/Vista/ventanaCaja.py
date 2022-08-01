from PyQt5 import QtWidgets, uic

class VentanaCaja(QtWidgets.QMainWindow):
      def __init__(self,parent = None):
            super(VentanaCaja,self).__init__(parent)
            uic.loadUi("Formulario/cajero.ui",self)
            self.btnRegistro.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page))
            self.btnPag2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
            self.btnPag3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_3))
            self.btnPag4.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
            self.btnPag5.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_5))
            self.setFixedWidth(956)
            self.setFixedHeight(714) 
            self.btnSalir.clicked.connect(self.Salir)
      def Salir(self):
            self.close()