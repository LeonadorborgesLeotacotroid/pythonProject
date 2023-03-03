import math
def calcular_identidadestrigonometricas(conversion):
    radianes=((conversion*math.pi)/180)
    return radianes
def calcular_identidadestrigonometricasseno(conversion):
    seno = math.sin((conversion*math.pi)/180)
    return seno
def calcular_identidadestrigonometricascoseno(conversion):
    coseno = math.cos((conversion*math.pi)/180)
    return coseno
def calcular_identidadestrigonometricastangente(conversion):
    tangente = math.tan((conversion*math.pi)/180)
    return tangente
#Pedimos un numero
def sinletras(cadena):  # palabra reservada que indica a Python que una nueva función está siendo definida
    try:  # PROBAR
        float(cadena)
        str(cadena)# PROBAR SI CADENA STRING ES UN FLOAT RETURNA A VERDADERA
        return True
    except ValueError:  # DE TODOS LOS ERRORES DE CADENA RETURNA FALSO
        return False
while (True):
   grados =input("Introduce un numero: ")
   if sinletras(grados):  # SI LA VARIABLE NUM CUMPLE LA FUNCION DEF
    conversion = float(grados)  # EL STRING O CADENA SE CONVIERTE A NUMERICO
    # calculamos las identidades utilizando la funcion de abstraccion
    dato1 = calcular_identidadestrigonometricas(conversion)
    dato2 = calcular_identidadestrigonometricasseno(conversion)
    dato3 = calcular_identidadestrigonometricascoseno(conversion)
    dato4 = calcular_identidadestrigonometricastangente(conversion)
    print("La conversion en radianes: ", dato1)
    print("La conversion en seno es: ", dato2)
    print("La conversion en coseno es: ", dato3)
    print("La conversion en tangente es:", dato4)
   else:
    print("***USTED NO ESCRIBIO UN NUMERO CORRECTAMENTE, INTENTELO NUEVAMENTE***")
    op = input("Tecleea S si quiere salir del programa\n si quiere continuar presione cualquier tecla: ")[:1]
    conversion3 = str(op)
    if op == "s" or op == "S":
        break




