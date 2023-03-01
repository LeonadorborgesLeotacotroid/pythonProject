#Elabora un programa en la que el usuario teclee 10 numeros ; contar los NUMEROS pares y los no pares
c1=0
c2=0
c3=0

for i in range(10):
    m = int(input("Introduce un numero: "))
    if m==0:
        c3 += 1
    else:
           if m % 2 == 0:
               c1 += 1
           else:
               c2 += 1
print("Esta es la cantidad de numeros pares: ", c1)
print("Esta la cantidad de numeros que no son pares: ", c2)
#BY Leonardo Melchor Borges Pech (LEOTACOTROID)
