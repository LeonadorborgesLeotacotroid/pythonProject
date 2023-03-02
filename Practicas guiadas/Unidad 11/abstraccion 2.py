import math
def suma_multiplicar (num1,num2, multiplicador):
    suma= num1 + num2
    resultado = suma * multiplicador
    return resultado
resultado = suma_multiplicar(3,5,2)
print(resultado)

#AREA DEL CIRCULO

def calcular_areaCirculo(radio):
    area = math.pi *(radio**2)
    return area

#Pedimos el radio del circulo al usuario
radio = float(input("Introduce el radio del circulo: "))

#calculamos el area del circulo utilizando la funcion de abstraccion
area = calcular_areaCirculo(radio)

print("El area del circulo es: ", area)

#---------------------------SIN ABSTRACCION----------------------------------------------
num1 = 3
num2 = 5
multiplicador = 2

suma = num1 + num2
resultado = suma * multiplicador
print(resultado)
# Calculamos el área del círculo
 # Pedimos el radio del círculo al usuario
radio = float(input("Introduce el radio del círculo: "))
# Calculamos el área del círculo
pi = 3.1416
area = pi * (radio ** 2)
# Mostramos el resultado al usuario
print("El área del círculo es:", area)