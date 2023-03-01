class Laptop():
    """
    Clase empleada para trabajar con Laptops
    """
    def __init__(self, marca, procesador, memoria = 16):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria

    def especificaciones(self):
        print("Esta laptop " + self.marca + "  cuenta con un procesador " +self.procesador,"esta cantidad de ram "+str(self.memoria))
laptop1 = Laptop('Dell', 'Core i7')
laptop1.especificaciones()