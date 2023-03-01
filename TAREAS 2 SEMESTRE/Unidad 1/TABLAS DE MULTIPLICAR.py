def sinletras(cadena):  # palabra reservada que indica a Python que una nueva función está siendo definida
    try:  # PROBAR
        float(cadena)
        int(cadena)
        str(cadena)  # PROBAR SI CADENA STRING ES UN FLOAT RETURNA A VERDADERA
        return True
    except ValueError:  # DE TODOS LOS ERRORES DE CADENA RETURNA FALSO
        return False


while (True):  # while sirve para validar el def

    numero = input("ESCRIBA EL NUMERO QUE DESEA MULTIPLICAR del 0 AL 10: ")
    rango = input("ESCRIBA HASTA DONDE TERMINARA LA MULTIPLICACION\nSOLO ENTEROS SI NO SE REPETIRA: ")

    if sinletras(numero) and sinletras(rango):  # SI LA VARIABLE NUM CUMPLE LA FUNCION DEF
        conversion = float(numero)  # EL STRING O CADENA SE CONVIERTE A NUMERICO
        conversion2 = int(rango)

        for i in range(0, conversion2 + 1):
            print(numero, "*", i, "=", conversion * i)  # EJECUCION DE LAS TABLAS DE MULTIPLICAR
    else:
        print("***USTED NO ESCRIBIO UN NUMERO CORRECTAMENTE, INTENTELO NUEVAMENTE***")
        op = input("Tecleea S si quiere salir del programa\n si quiere continuar presione cualquier tecla: ")[:1]
        conversion3 = str(op)

        if op == "s" or op == "S":
            break
