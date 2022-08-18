from Controlador.registroPedido import RegPedido

class ArregloRegPedido:


      def __init__(self):
            self.dataPedido = []
            self.cargarPedido()

      def adicionaRegPedido(self, objPedido):
            self.dataPedido.append(objPedido)

      def devolverRegPedido(self, pos):
            return self.dataPedido[pos]
      
      def tamañoArregloRegPedido(self):
            return len(self.dataPedido)

      def buscarRegPedido(self, Pedido):
            for i in range(self.tamañoArregloRegPedido()):
                  if Pedido == self.dataPedido[i].getCategoria():
                        return i
            return -1

      def eliminarRegPedido(self, indice):
            del(self.dataPedido[indice])
            
      def modificarRegPedido(self, objPedido, pos):
            self.dataPedido[pos]=objPedido
      
      def retornarDatos(self):
            return self.dataPedido
      

      def cargarPedido(self):
            archivo = open("Dato/RegistroDelPedido.txt", "r", encoding = "utf-8")
            for linea in archivo.readlines():
                  columna = str(linea).split(",")
                  pedidoDni = columna[0]
                  producto = columna[1]
                  descripcion = columna[2]
                  precio = columna[3]
                  cantidad = columna[4]
                  descuento=columna[5].strip()
                  objPedido = RegPedido(pedidoDni,producto, descripcion, precio, cantidad,descuento)
                  self.adicionaRegPedido(objPedido)
            archivo.close()

      def grabarPedido(self):
            archivo = open("Dato/RegistroDelPedido.txt", "w+", encoding = "utf-8")
            for i in range(self.tamañoArregloRegPedido()):
                  archivo.write(str(self.devolverRegPedido(i).getPedidoDNI()) + ","
                  + str(self.devolverRegPedido(i).getPedidoProducto()) + "," 
                  + str(self.devolverRegPedido(i).getPedidoDescripcion()) + ","
                  + str(self.devolverRegPedido(i).getPrecio()) + ","
                  + str(self.devolverRegPedido(i).getCantidad()) + ","
                  + str(self.devolverRegPedido(i).getDescuento()) + "\n")
            archivo.close()
            

            