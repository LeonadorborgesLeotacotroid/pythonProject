class Sistema:
    def __init__(self):
        pass

    def celular(self, sistema='android'):
        self._Presionar_botonOn(sistema)
        self._Presentarlogo()
        self._SesionUser()

    def _Presionar_botonOn(self, sistema):
        print(f'Cargando sistema operativo del telefono {sistema}')

    def _Presentarlogo(self):
        print('Mostrando en pantalla logo del sistema')

    def _SesionUser(self):
        print('Presentando pantalla inicio de sesion')


phone = Sistema()
phone.celular()
