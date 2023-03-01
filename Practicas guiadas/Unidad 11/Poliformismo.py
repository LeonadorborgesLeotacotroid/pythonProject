class Animal:
    def __init__(self, name):
        self.name = name

    def hacerSonido(self):
        pass #Es un pase,el método no puede estar vacio


class Perro(Animal):
    def hacerSonido(self):
        return f"{self.name} dice Guau!"


class Gato(Animal):
    def hacerSonido(self):
        return f"{self.name} dice Meow!"


dog = Perro("Fido")
cat = Gato("Fluffy")

print(dog.hacerSonido())
print(cat.hacerSonido())