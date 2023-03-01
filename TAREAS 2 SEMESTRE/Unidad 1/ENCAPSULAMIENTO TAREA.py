class Sesion:
    def __init__(self, nickname, contraseña):
        self.nickname = nickname
        self.__contraseña = contraseña #es tenerlo privado

    def get_contraseña(self):
        return self.__contraseña

    def set_contraseña(self, nueva_contraseña):
        if nueva_contraseña == 12345:
            self.__contraseña = nueva_contraseña
        else:
            print("Error de contraseña.")

s1 = Sesion("Leotaco",1234)
print(s1.nickname) #SE IMPRIMIRA EL NICKNAME
print(s1.get_contraseña()) #SE MOSTRARA LA CONTRASEÑA PREESCRITA

# Intentamos modificar la contraseña pero en negativo, lo que no se debe hacer por encapsulamiento.
s1.__contraseña = -1234
print(s1.get_contraseña())   # Output: 1234, debera monstrar la contraseña correcta

# Utilizamos el método set_contraseña para modificar la contraseña.
s1.set_contraseña(1245)   # Output: "La contraseña debe ser igual a 1234."

