class RegistroCliente():
      #Atributos de la pagina cliente
      __RegistroDNI = 0
      __RegistroNombre = ""
      __RegistroApellidoP = ""
      __RegistroApellidoM = ""
      __RegistroTelefono = 0
      __RegistroCorreo = ""
      
      #Metodo constructor
      def __init__(self,registroDNI,registroNombre,registroApellidoP,registroApellidoM,registroTelefono,registroCorreo):
            self.__RegistroDNI=registroDNI
            self.__RegistroNombre=registroNombre
            self.__RegistroApellidoP=registroApellidoP
            self.__RegistroApellidoM=registroApellidoM
            self.__RegistroTelefono=registroTelefono
            self.__RegistroCorreo=registroCorreo
      
      #Metodos get
      def getRegistroDNI(self):
            return self.__RegistroDNI
      
      def getRegistroNombre(self):
            return self.__RegistroNombre
      
      def getRegistroApellidoP(self):
            return self.__RegistroApellidoP
      
      def getRegistroApellidoM(self):
            return self.__RegistroApellidoM
      
      def getRegistroTelefono(self):
            return self.__RegistroTelefono
      
      def getRegistroCorreo(self):
            return self.__RegistroCorreo
      
      
      #Metodos set
      def setRegistroDNI(self,registroDNI):
            self.__RegistroDNI=registroDNI
            
      def setRegistroNombre(self,registroNombre):
            self.__RegistroNombre=registroNombre
            
      def setRegistroApellidoP(self,registroApellidoP):
            self.__RegistroApellidoP=registroApellidoP
            
      def setRegistroApellidoM(self,registroApellidoM):
            self.__RegistroApellidoM=registroApellidoM
            
      def setRegistroTelefono(self,registroTelefono):
            self.__RegistroTelefono=registroTelefono
            
      def setRegistroCorreo(self,registroCorreo):
            self.__RegistroCorreo=registroCorreo