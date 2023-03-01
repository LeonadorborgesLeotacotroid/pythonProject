#Practica 10/02/2023
#Que el usuario teclee su edad determinando si es mayor o de menor de edad y/o participa en un programa
while True:
   print("HOLA INGRESA UNA DE LAS SIGUIENTES OPCIONES: ")
   print("#PRESIONE 1: Si mediante su edad tiene opurtunidad de participar en su programa.\n#PRESIONA 2: Si Desea Saber SI ALCANZASTE TU AHORRO.\n#PRESIONE 3: Si desea saber Tu Nivel de Ingles")
   opc=int(input("¿Cual opcion desea ejecutar?: "))
   if opc==1:
    edad=int(input("---Hola,teclea tu edad actual---: ")[:2])
    if edad<18:
        print("---Eres menor de edad---")
    elif edad>=18 and edad<65:
         print("---Eres mayor de edad---")
    else:
         print("---Eres mayor de edad y tienes derecho al programa de 65+---")
   elif opc==2: #Aqui empieza el segundo programa
    ahorro=float(input("HOLA ESCRIBE TU META DE AHORRO QUE DESEA ALCANZAR: "))
    estado=float(input("Escribe la cantidad actual que tienes: "))
    if ahorro==estado:
        print("-------Felicidades llego a su meta--------")
    elif ahorro>estado:
        Cambio1=ahorro-estado
        print("---Lamentablemente NO HAS LLEGADO A TU META, POR LO QUE NECESITARA ESTA CANTIDAD PARA LOGRARLO:--- ", Cambio1)
    else:
        Cambio2=estado-ahorro
        print( "-----FELICIDADES LLEGASTE A LA META Y TE SOBRARA ESTA CANTIDAD: -----", Cambio2)
   elif opc==3: #Aqui empieza el 3 programa
                   a = int(input(" Ingrese tu nivel de ingles, segun el examen de prueba que seleccionaste\n recuerda que los niveles son del 0 al 10: ")[:2])
                   if a>=0 and a<=3:
                       print("-----Tienes un nivel bajo----")
                   else:
                            if a>=4 and a<=7:
                               print("------Tienes un nivel medio-----")
                            else:
                                     if a>=8 and a<=9:
                                         print("-----Tienes un nivel bueno------")
                                     else:
                                         print("----Tienes nivel avanzado-----")
   else:
        print("----USTED ELIGIO EL NUMERO EQUIVOCADO... ESPERE A QUE REINCIE EL PROGRAMA----")
   con=input("*TECLEE S al finalizar el programa si desea salir despues de ejecutar este programa\n*PULSE CUALQUIER TECLA SI QUIERE CONTINUAR O ESCRIBIO EL NUMERO EQUIVOCADO: ")
   if con=='S' or con=='s':
      break
#By Leonardo Melchor Borges Pech (Leotacotroid)
