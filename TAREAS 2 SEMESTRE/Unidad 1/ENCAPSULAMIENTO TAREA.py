class Escuela:

     def __init__(self, nombre, escolaridad, localidad):
            self.nombre = nombre
            self.escolaridad = escolaridad
            self.__localidad= localidad

     def mostrar(self):
         print("ESCUELA: "+self.nombre)
         print("ESCUELA: " + self.escolaridad)
         print("ESCUELA: " + self.__localidad)#PRIVADO

#GET=OBTENER Y SET= ASIGNAR
     def get_localidad(self):
         return self.__localidad

     def set_localidad(self,localidad):
         self.__localidad = localidad

#obtener localidad
e1=Escuela("COBAY", "BACHILLERATO", "PROGRESO")
localidad = e1.get_localidad()
print(localidad)
#cambiar ubicacion metodo set
e1.set_localidad("Merida")
e1.mostrar()

#AQUI ESTA PARTE DEL ALGORITMO ES PARA DEMOSTRAR QUE LA VARIABLE LOCALIDAD ESTA
#ENCAPSULADO POR ENDE DA ERROR
'''e2=Escuela("MANIOBRAS MARITIMA", "PRIMARIA", "PROGRESO")
print(e2.__localidad())
e2.mostrar()'''