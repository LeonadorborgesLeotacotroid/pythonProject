class Usuarios:
    def __init__(datos, nid, nickname, nombre):  # Cambia la palabra self por *datos*
        datos.nid = nid
        datos.nickname = nickname
        datos.nombre = nombre

    def muestra_Datos(datos):
        print("El nombre del usuario es : " + datos.nombre)
        print("El ID de usuario es: " + datos.nid)
        print("El alias del usuario es: " + datos.nickname)


class UsuariosGold(Usuarios):
    def __init__(datos, nid, nickname, nombre, multiplayer):
        super().__init__(nid, nickname, nombre)
        multiplayer = "ACTIVO PUEDES TENER MULTIJUGADOR EN LINEA SIN PROBLEMAS"
        datos.multiplayer = multiplayer

    def muestra_Datos(datos):
        super().muestra_Datos()
        print(f"XBOX LIVE GOLD: {datos.multiplayer}")


class UsuariosGamepass(Usuarios):
    def __init__(datos, nid, nickname, nombre, libreria, ):
        super().__init__(nid, nickname, nombre)
        libreria = "ACTIVO ADEMAS DEL MULTIJUGADOR FREE TIENES CATALOGO DE JUEGOS GRATIS"
        datos.libreria = libreria

    def muestra_Datos(datos):
        super().muestra_Datos()
        print(f"XBOX GAMEPASS: {datos.libreria}")


user0 = Usuarios("98", "T4ÑA", "Taya")
user0.muestra_Datos()
print("---------------------------------------------------------------------------------")
user1 = UsuariosGold("78", "Leotaco", "Leonardo", "SI")
user1.muestra_Datos()
print("---------------------------------------------------------------------------------")
user2 = UsuariosGamepass("128", "god_GH0ST18", "Carlos", "SI", )
user2.muestra_Datos()



