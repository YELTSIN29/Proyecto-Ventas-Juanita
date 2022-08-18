
class RegProducto():
      #Atributos del Registro Producto
      __CodProducto=0
      __Categoria=""
      __Descripcion=""
      __Cantidad=0
      __Precio=0
      #Constructor
      def __init__(self,codProducto,categoria,descripcion,cantidad,precio):
            self.__CodProducto=codProducto
            self.__Categoria=categoria
            self.__Descripcion=descripcion
            self.__Cantidad=cantidad
            self.__Precio=precio
      
      #Metodo get
      def getCodProducto(self):
            return self.__CodProducto
      def getCategoria(self):
            return self.__Categoria
      def getDecripcion(self):
            return self.__Descripcion
      def getCantidad(self):
            return self.__Cantidad
      def getPrecio(self):
            return self.__Precio
      
      #Metodo set
      def setCodProducto(self,codProducto):
            self.__CodProducto=codProducto
      def setCategoria(self,categoria):
            self.__Categoria=categoria
      def setDecripcion(self,descripcion):
            self.__Descripcion=descripcion
      def setCantidad(self,cantidad):
            self.__Cantidad=cantidad
      def setPrecio(self,precio):
            self.__Precio=precio