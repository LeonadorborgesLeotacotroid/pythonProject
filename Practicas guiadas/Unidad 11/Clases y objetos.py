#clases y objetos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludarPersona(self):
        print("Hola, mi nombre es " + self.nombre + " y tengo " + str(self.edad) + " años.")

person = Persona("Ligia",43)
person.saludarPersona()

#clases y objetos2

class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def __init__(self, nom, ed, curp):
        self.nombre = nom
        self.edad = ed
        self.curp = curp

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona('Ligia', 42, 'CURP')
objetoPersona.mostrarDatos()