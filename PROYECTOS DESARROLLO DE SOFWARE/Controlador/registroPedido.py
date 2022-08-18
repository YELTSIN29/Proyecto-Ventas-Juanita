class RegPedido():
      #Atributos del Registro Pedido
      __PedidoDNI=0
      __PedidoProducto=''
      __PedidoDescripcion=''
      __Precio=0
      __Cantidad=0
      __Descuento=0
      #Constructor
      def __init__(self,pedidoDni,pedidoProducto,pedidoDescripcion,cantidad,precio,descuento):
            self.__PedidoDNI=pedidoDni
            self.__PedidoProducto=pedidoProducto
            self.__PedidoDescripcion=pedidoDescripcion
            self.__Precio=precio
            self.__Cantidad=cantidad
            self.__Descuento=descuento
            
      
      #Metodo get
      def getPedidoDNI(self):
            return self.__PedidoDNI
      def getPedidoProducto(self):
            return self.__PedidoProducto
      def getPedidoDescripcion(self):
            return self.__PedidoDescripcion
      def getCantidad(self):
            return self.__Cantidad
      def getPrecio(self):
            return self.__Precio
      def getDescuento(self):
            return self.__Descuento
      
      #Metodo set
      def setPedidoDNI(self,PedidoDni):
            self.__PedidoDNI=PedidoDni
      def setPedidoProducto(self,pedidoProducto):
            self.__PedidoProducto=pedidoProducto
      def setPedidoDescripcion(self,descripcion):
            self.__Descripcion=descripcion
      def setCantidad(self,cantidad):
            self.__Cantidad=cantidad
      def setPrecio(self,precio):
            self.__Precio=precio
      def setDescuento(self,descuento):
            self.__Descuento=descuento