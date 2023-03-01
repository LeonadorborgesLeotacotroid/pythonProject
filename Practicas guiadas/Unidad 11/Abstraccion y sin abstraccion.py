#con asbtraccion

def sumar_Numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
print(sumar_Numeros(numeros))

#sin abstraccion

numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero
print(suma)