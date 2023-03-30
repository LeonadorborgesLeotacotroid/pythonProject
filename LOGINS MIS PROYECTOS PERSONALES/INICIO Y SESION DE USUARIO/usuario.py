class usuario():

    numUsuarios = 0
    def __init__(self,nombre,password):
        self.nombre=nombre
        self.password=password

        self.conectado=False
        self.intentos=3

        usuario.numUsuarios+=1

    def conectar(self):
        mycontraseña=input("INGRESE SU CONTRASEÑA")
        if mycontraseña==self.password:
            print("sesion con exito")
            self.conectado=True
        else:
             self.intentos-=1
             if self.intentos>0:
                  print("CONTRASEÑA INCORRECTA, INTENTALO NUEVAMENTE")
                  print("intentos restantes", self.intentos)
                  self.conectar()
             else:
                 print("Error, no se puede iniciar sesion")
                 print("ADIIOS")


    def desconectar(self):
        if self.conectado:
            print("sesion cerrada, con exito")
            self.conectado=False
        else:
            print("no inicio sesion")


    def __str__(self):
        if self.conectado:
            conect="conectado"
        else:
            conect="desconectado"
        return f"Mi nombre de usuariio es {self.nombre} y estoy {conect}"

user1=usuario(input("ingrese un nombre: "), input("ingrese su contraseña"))
print(user1)

user1.conectar()
print(user1)

user1.desconectar()
print(user1)
