#03/03/2023
class Persona: #CLASE PRINCIPAL
    champ=" "
    nombre = "" #atributos
    edad = ""
    def  __init__(self): #METODO
        self.nombre = input('Ingrese su nombre ')
        self.edad = int(input('Ingrese su edad: '))
        print(f'Hola {self.nombre} tienes {self.edad} años , gracias por participar en este programa')
class Estudiante(Persona): #HERENCIA DE CLASES de persona
    def promedio_final(calf1,calf2,calf3):
        pro = (((calf1+calf2+calf3) / 3)) #abstraccion
        return pro
class Docente(Persona):
    def salario_final(horas,horas2,):
        salfinal= (horas*horas2)
        return salfinal

print("HOLA INGRESE UN NUMERO SI ERES UN ESTUDIANTE O DOCENTE")
print("-----------------------------------------")
print("PRESIONE (1) SI ERES UN ESTUDIANTE")
print("PRESIONE (2) SI UN MAESTRO")
decision =int(input("ESCRIBA LA OPCION FINAL "))

if decision == 1:
    champ=Estudiante()#llamando clase estudiante
    calf1=int(input("HOLA iingresa tu primera calificacion: "))
    calf2=int(input("HOLA iingresa tu segunda calificacion: "))
    calf3=int(input("HOLA iingresa tu tercera calificacion: "))
    dato1=Estudiante.promedio_final(calf1,calf2,calf3)#llamando al metodo de abstraccion
    print("su promedio final es", +dato1)

elif decision == 2:
    champ=Docente()
    hora = int(input("HOLA lo que ganas por hora: "))
    hora1 = int(input("HOLA las horas que trabajas: "))
    dato1 = Docente.salario_final(hora, hora1)
    print("su salario final", +dato1)

else:
    print("ERROR")





