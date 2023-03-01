class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def imprimirInfo(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def imprimirInfo(self):
        super().imprimirInfo()
        print(f"Número de puertas: {self.num_puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    def imprimirInfo(self):
        super().imprimirInfo()
        print(f"Cilindrada: {self.cilindrada}")

mi_coche = Coche("Ford", "Mustang", 2020, 2)
mi_coche.imprimirInfo()  # Imprime "Marca: Ford, Modelo: Mustang, Año: 2020" seguido de "Número de puertas: 2"

mi_moto = Moto("Harley-Davidson", "Fat Bob", 2021, 1868)
mi_moto.imprimirInfo()  # Imprime "Marca: Harley-Davidson, Modelo: Fat Bob, Año: 2021" seguido de "Cilindrada: 1868"