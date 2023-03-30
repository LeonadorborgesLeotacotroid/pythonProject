class Alumno:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def setEdad(self, ed):
        self._edad = ed

    def getEdad(self):
        return self._edad

    def setNombre(self, nom):
        self._nombre = nom

    def getNombre(self):
        return self._nombre