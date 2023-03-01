class Campeones:
    champ=" "
    def __init__(self):
        self.champ="su campeon es: "
    def anunciar(self):
        pass  # es un pase el metodo, el metodo no puede estar vacio

class WWE(Campeones):
    def anunciar(self):
        return f"EL MAXIMO CAMPEON MUNDIAL ES EL JEFE TRIBAL ROMAN REIGNS"

class NJPW(Campeones):
    def dezplazamiento(self):
        return f"El MAXIMO CAMPEON MUNDIAL ES EL *RAINMAKER* KAZUCHIKA OKADA"

class AEW(Campeones):
    def anunciar(self):
        return f"El MAXIMO CAMPEON MUNDIAL es Maxwell Jacob Friedman MJF"

class AAA(Campeones):
    def anunciar(self):
        return f"El MAXIMO CAMPEON MUNDIAL es EL HIJO DE VIKINGO"

def sinletras(cadena):  # palabra reservada que indica a Python que una nueva función está siendo definida
    try:  # PROBAR
        int(cadena)
        str(cadena)# PROBAR SI CADENA STRING ES UN FLOAT RETURNA A VERDADERA
        return True
    except ValueError:  # DE TODOS LOS ERRORES DE CADENA RETURNA FALSO
        return False

while (True):  # while sirve para validar el def
    print("HOLA INGRESE UN NUMERO SI QUIERE SABER EL CAMPEON MAXIMO DE CADA EMPRESA DE WRESTLING")
    print("-----------------------------------------")
    print("PRESIONE (1) SI QUIERES SABER EL CAMPEON MAXIMO DE WWE")
    print("PRESIONE (2) SI QUIERES SABER EL CAMPEON MAXIMO DE WWE")
    print("PRESIONE (3) SI QUIERES SABER EL CAMPEON MAXIMO DE WWE")
    print("PRESIONE (4) SI QUIERES SABER EL CAMPEON MAXIMO DE WWE")

    decision = input("ESCRIBA LA OPCION FINAL ")
    if sinletras(decision):# SI LA VARIABLE NUM CUMPLE LA FUNCION DEF
        conversion = int(decision) # EL STRING O CADENA SE CONVIERTE A NUMERICO
        if conversion == 1:
          champ=WWE()
          print(champ.anunciar())
        elif conversion == 2:
          champ = NJPW()
          print(champ.anunciar())
        elif conversion == 3:
          champ = AEW()
          print(champ.anunciar())
        elif conversion == 4:
          champ = AAA()
          print(champ.anunciar())
    else:
        print("***USTED NO ESCRIBIO UN NUMERO CORRECTAMENTE, INTENTELO NUEVAMENTE***")
        op = input("Tecleea S si quiere salir del programa\n si quiere continuar presione cualquier tecla: ")[:1]
        conversion3 = str(op)

        if op == "s" or op == "S":
            break



