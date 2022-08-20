from Controlador.registroTrabajador import RegistroTrabajador



class ArregloTrabajador:


      def __init__(self):
            self.dataTrabajador = []
            self.cargarTrabajador()

      def adicionaTrabajador(self, objTrabajador):
            self.dataTrabajador.append(objTrabajador)

      def devolverTrabajador(self, pos):
            return self.dataTrabajador[pos]
      
      def tamañoArregloTrabajador(self):
            return len(self.dataTrabajador)

      def buscarTrabajador(self, dni):
            for i in range(self.tamañoArregloTrabajador()):
                  if dni == self.dataTrabajador[i].getRegistroDNI():
                        return i
            return -1

      def eliminarTrabajador(self, indice):
            del(self.dataTrabajador[indice])
            
      def modificarTrabajador(self, objTrabajador, pos):
            self.dataTrabajador[pos]=objTrabajador
      
      def retornarDatos(self):
            return self.dataTrabajador
      

      def cargarTrabajador(self):
            archivo = open("Dato/RegistroDelTrabajador.txt", "r", encoding = "utf-8")
            for linea in archivo.readlines():
                  columna = str(linea).split(",")
                  dni = columna[0]
                  nombre = columna[1]
                  apellidoP = columna[2]
                  apellidoM = columna[3]
                  telefono = columna[4]
                  correo = columna[5]
                  cargo = columna[6]
                  sueldo = columna[7].strip()
                  objTrabajador = RegistroTrabajador(dni,nombre, apellidoP, apellidoM, telefono,correo,cargo,sueldo)
                  self.adicionaTrabajador(objTrabajador)
            archivo.close()

      def grabarTrabajador(self):
            archivo = open("Dato/RegistroDelTrabajador.txt", "w+", encoding = "utf-8")
            for i in range(self.tamañoArregloTrabajador()):
                  archivo.write(str(self.devolverTrabajador(i).getRegistroTrabDNI()) + ","
                  + str(self.devolverTrabajador(i).getRegistroTrabNombre()) + "," 
                  + str(self.devolverTrabajador(i).getRegistroTrabApellidoP()) + ","
                  + str(self.devolverTrabajador(i).getRegistroTrabApellidoM()) + ","
                  + str(self.devolverTrabajador(i).getRegistroTrabTelefono()) + ","
                  + str(self.devolverTrabajador(i).getRegistroTrabCorreo()) + ","
                  + str(self.devolverTrabajador(i).getRegistroTrabCargo()) + ","
                  + str(self.devolverTrabajador(i).getRegistroTrabSueldo()) + "\n")
            archivo.close()