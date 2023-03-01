

opc=int(input("¿Cual opcion desea ejecutar?: "))
if opc==1:
    edad=int(input("---Hola,teclea tu edad actual---: ")[:2])
    if edad<18:
        print("---Eres menor de edad---")
    else:
            if edad>=18 and edad<65:
                    print("---Eres mayor de edad---")
            else:
                   print("---Eres mayor de edad y tienes derecho al programa de 65+---")