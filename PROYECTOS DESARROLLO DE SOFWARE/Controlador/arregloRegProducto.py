from Controlador.registroProducto import RegProducto

class ArregloRegProducto:


      def __init__(self):
            self.dataProducto = []
            self.cargarProducto()

      def adicionaRegProducto(self, objProducto):
            self.dataProducto.append(objProducto)

      def devolverRegProducto(self, pos):
            return self.dataProducto[pos]
      
      def tamañoArregloRegProducto(self):
            return len(self.dataProducto)

      def buscarRegProducto(self, producto):
            for i in range(self.tamañoArregloRegProducto()):
                  if producto == self.dataProducto[i].getCodProducto():
                        return i
            return -1

      def eliminarRegProducto(self, indice):
            del(self.dataProducto[indice])
            
      def modificarRegProducto(self, objProducto, pos):
            self.dataProducto[pos]=objProducto
      
      def retornarDatos(self):
            return self.dataProducto
      

      def cargarProducto(self):
            archivo = open("Dato/RegistroDelProducto.txt", "w+", encoding = "utf-8")
            for linea in archivo.readlines():
                  columna = str(linea).split(",")
                  codProducto = columna[0]
                  categoria = columna[1]
                  descripcion = columna[2]
                  cantidad = columna[3]
                  precio = columna[4].strip()
                  objProd = RegProducto(codProducto,categoria, descripcion, cantidad, precio)
                  self.adicionaRegProducto(objProd)
            archivo.close()

      def grabarProducto(self):
            archivo = open("Dato/RegistroDelProducto.txt", "w+", encoding = "utf-8")
            for i in range(self.tamañoArregloRegProducto()):
                  archivo.write(str(self.devolverRegProducto(i).getCodProducto()) + ","
                  + str(self.devolverRegProducto(i).getCategoria()) + "," 
                  + str(self.devolverRegProducto(i).getDecripcion()) + ","
                  + str(self.devolverRegProducto(i).getCantidad()) + ","
                  + str(self.devolverRegProducto(i).getPrecio()) + "\n")
            archivo.close()
