from Controlador.registroCliente import Registro



class ArregloVentas:


      def __init__(self):
            self.dataClientes = []
            self.cargarCliente()

      def adicionaCliente(self, objCli):
            self.dataClientes.append(objCli)

      def devolverCliente(self, pos):
            return self.dataClientes[pos]
      
      def tamañoArregloCliente(self):
            return len(self.dataClientes)

      def buscarCliente(self, dni):
            for i in range(self.tamañoArregloCliente()):
                  if dni == self.dataClientes[i].getRegistroDNI():
                        return i
            return -1

      def eliminarCliente(self, indice):
            del(self.dataClientes[indice])
            
      def modificarCliente(self, objCli, pos):
            self.dataClientes[pos]=objCli
      
      def retornarDatos(self):
            return self.dataClientes
      

      def cargarCliente(self):
            archivo = open("Dato/RegistroDelCliente.txt", "r", encoding = "utf-8")
            for linea in archivo.readlines():
                  columna = str(linea).split(",")
                  dni = columna[0]
                  nombre = columna[1]
                  apellidoP = columna[2]
                  apellidoM = columna[3]
                  telefono = columna[4]
                  correo = columna[5].strip()
                  objCli = Registro(dni,nombre, apellidoP, apellidoM, telefono,correo)
                  self.adicionaCliente(objCli)
            archivo.close()

      def grabarCliente(self):
            archivo = open("Dato/RegistroDelCliente.txt", "w+", encoding = "utf-8")
            for i in range(self.tamañoArregloCliente()):
                  archivo.write(str(self.devolverCliente(i).getRegistroDNI()) + ","
                  + str(self.devolverCliente(i).getRegistroNombre()) + "," 
                  + str(self.devolverCliente(i).getRegistroApellidoP()) + ","
                  + str(self.devolverCliente(i).getRegistroApellidoM()) + ","
                  + str(self.devolverCliente(i).getRegistroTelefono()) + ","
                  + str(self.devolverCliente(i).getRegistroCorreo()) + "\n")
            archivo.close()
      
     
      