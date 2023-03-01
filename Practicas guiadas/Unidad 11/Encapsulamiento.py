class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad #es tenerlo privado

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor que cero.")
p = Persona("Ligia", 30)

print(p.nombre)   # Output: "Ligia"
print(p.get_edad())   # Output: 30

# Intentamos modificar la edad directamente, lo que no se debe hacer por encapsulamiento.
p.__edad = -10
print(p.get_edad())   # Output: 30, la edad no ha sido modificada.

# Utilizamos el método set_edad para modificar la edad.
p.set_edad(-10)   # Output: "La edad debe ser mayor que cero."
print(p.get_edad())   # Output: 30, la edad no ha sido modificada.
p.set_edad(40)
print(p.get_edad())   # Output: 40