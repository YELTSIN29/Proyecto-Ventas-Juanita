class RegistroTrabajador():
      #Atributos de la pagina cliente
      __RegistroTrabajadorDNI = 0
      __RegistroTrabajadorNombre = ""
      __RegistroTrabajadorApellidoP = ""
      __RegistroTrabajadorApellidoM = ""
      __RegistroTrabajadorTelefono = 0
      __RegistroTrabajadorCorreo = ""
      __RegistroTrabajadorCargo=''
      __RegistroTrabajadorSueldo=0.0
      
      #Metodo constructor
      def __init__(self,registroTrabajadorDNI,registroTrabajadorNombre,registroTrabajadorApellidoP,registroTrabajadorApellidoM,registroTrabajadorTelefono,registroTrabajadorCorreo,registroTrabajadorCargo,registroTrabajadorSueldo):
            self.__RegistroTrabajadorDNI=registroTrabajadorDNI
            self.__RegistroTrabajadorNombre=registroTrabajadorNombre
            self.__RegistroTrabajadorApellidoP=registroTrabajadorApellidoP
            self.__RegistroTrabajadorApellidoM=registroTrabajadorApellidoM
            self.__RegistroTrabajadorTelefono=registroTrabajadorTelefono
            self.__RegistroTrabajadorCorreo=registroTrabajadorCorreo
            self.__RegistroTrabajadorCargo=registroTrabajadorCargo
            self.__RegistroTrabajadorSueldo=registroTrabajadorSueldo
      
      #Metodos get
      def getRegistroTrabDNI(self):
            return self.__RegistroTrabajadorDNI
      
      def getRegistroTrabNombre(self):
            return self.__RegistroTrabajadorNombre
      
      def getRegistroTrabApellidoP(self):
            return self.__RegistroTrabajadorApellidoP
      
      def getRegistroTrabApellidoM(self):
            return self.__RegistroTrabajadorApellidoM
      
      def getRegistroTrabTelefono(self):
            return self.__RegistroTrabajadorTelefono
      
      def getRegistroTrabCorreo(self):
            return self.__RegistroTrabajadorCorreo
      
      def getRegistroTrabCargo(self):
            return self.__RegistroTrabajadorCargo
      
      def getRegistroTrabSueldo(self):
            return self.__RegistroTrabajadorSueldo
      
      
      #Metodos set
      def setRegistroTrabDNI(self,registroTrabajadorDNI):
            self.__RegistroTrabajadorDNI=registroTrabajadorDNI
            
      def setRegistroTrabNombre(self,registroTrabajadorNombre):
            self.__RegistroTrabajadorNombre=registroTrabajadorNombre
            
      def setRegistroTrabApellidoP(self,registroTrabajadorApellidoP):
            self.__RegistroTrabajadorApellidoP=registroTrabajadorApellidoP
            
      def setRegistroTrabApellidoM(self,registroTrabajadorApellidoM):
            self.__RegistroTrabajadorApellidoM=registroTrabajadorApellidoM
            
      def setRegistroTrabTelefono(self,registroTrabajadorTelefono):
            self.__RegistroTrabajadorTelefono=registroTrabajadorTelefono
            
      def setRegistroTrabCorreo(self,registroTrabajadorCorreo):
            self.__RegistroTrabajadorCorreo=registroTrabajadorCorreo
            
      def setRegistroTrabCargo(self,registroTrabajadorCargo):
            self.__RegistroTrabajadorCargo=registroTrabajadorCargo
            
      def setRegistroTrabSueldo(self,registroTrabajadorSueldo):
            self.__RegistroTrabajadorSueldo=registroTrabajadorSueldo