class Pieza(object):
    def __init__(self, tipo, color1 = None, color2 = None, color3= None, color4= None, color5 = None, color6 = None):
        self.tipo = tipo
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        self.color5 = color5
        self.color6 = color6
        self.colores = [color1, color2, color3, color4, color5, color6]
        
    def __str__(self):
        respuesta = f"Pieza: {self.tipo}, Colores: "
        for color in self.colores:
            if color != None:
                respuesta += f"{color} "
        return respuesta


# Falta añadir la orientación de las piezas, para las aristas mete 0 o 1, para las esquinas 0, 1 o 2, centros no metas, ya que son invariantes y nucleo idem
class Esquina(Pieza):
    def __init__(self, color1, color2, color3, pos):
        super(Esquina, self).__init__("Esquina", color1, color2, color3, None, None, None)
        self.pos = pos

    def __str__(self):
        return f"{self.tipo} {self.pos} {self.color1} {self.color2} {self.color3}"
    
class Centro(Pieza):
    def __init__(self, color1, pos):
        super(Centro, self).__init__("Centro", color1, None, None, None, None, None)
        self.pos = pos

    def __str__(self):
        return f"{self.tipo} {self.pos} {self.color1}"
    
class Arista(Pieza):
    def __init__(self, color1, color2, pos):
        super(Arista, self).__init__("Arista", color1, color2, None, None, None, None)
        self.pos = pos

    def __str__(self):
        return f"{self.tipo} {self.pos} {self.color1} {self.color2}"
    
class Nucleo(Pieza):
    def __init__(self, pos):
        super(Nucleo, self).__init__("Nucleo", None, None, None, None, None, None)
        self.pos = pos

    def __str__(self):
        return f"{self.tipo} {self.pos} {self.color1}"

class Cubo(object):
    def __init__(self):
        """
        [[[], [], []], [[], [], []], [[], [], []]]
        [0, 1, 2]

            [0] => [[], [], []] -> Capa superior
                [0] => [esquina, arista, esquina]
                [1] => [arista, centro, arista]
                [2] => [esquina, arista, esquina]
            
            [1] => [[], [], []] -> Capa media
                [0] => [arista, centro, arista]
                [1] => [centro, nucleo, centro]
                [2] => [arista, centro, arista]

            [2] => [[], [], []] -> Capa inferior
                [0] => [esquina, arista, esquina]
                [1] => [arista, centro, arista]
                [2] => [esquina, arista, esquina]
        """
        self.capa_sup = []
        self.capa_mid = []
        self.capa_inf = []

        self.capa_sup.append([Esquina("Blanco", "Azul", "Rojo", 0), Arista("Blanco", "Azul", 1), Esquina("Blanco", "Naranja", "Azul", 2)])
        self.capa_sup.append([Arista("Blanco", "Rojo", 3), Centro("Blanco", 4), Arista("Blanco", "Verde", 5)])
        self.capa_sup.append([Esquina("Blanco", "Verde", "Naranja", 6), Arista("Blanco", "Naranja", 7), Esquina("Blanco", "Rojo", "Verde", 8)])

        self.capa_mid.append([Arista("Rojo", "Azul", 9), Centro("Azul", 10), Arista("Naranja", "Azul", 11)])
        self.capa_mid.append([Centro("Rojo", 12), Nucleo(13), Centro("Verde", 14)])
        self.capa_mid.append([Arista("Verde", "Rojo", 15), Centro("Naranja", 16), Arista("Azul", "Naranja", 17)])

        self.capa_inf.append([Esquina("Amarillo", "Azul", "Rojo", 18), Arista("Amarillo", "Rojo", 19), Esquina("Amarillo", "Naranja", "Azul", 20)])
        self.capa_inf.append([Arista("Amarillo", "Verde", 21), Centro("Amarillo", 22), Arista("Amarillo", "Azul", 23)])
        self.capa_inf.append([Esquina("Amarillo", "Verde", "Naranja", 24), Arista("Amarillo", "Naranja", 25), Esquina("Amarillo", "Rojo", "Verde", 26)])

        self.esquinas = []
        self.centros = []
        self.aristas = []

        self.aristas.append(Arista("Blanco", "Azul", 0))
        self.aristas.append(Arista("Blanco", "Rojo", 1))
        self.aristas.append(Arista("Blanco", "Verde", 2))
        self.aristas.append(Arista("Blanco", "Naranja", 3))
        self.aristas.append(Arista("Rojo", "Azul", 4))
        self.aristas.append(Arista("Azul", "Naranja", 5))
        self.aristas.append(Arista("Naranja", "Verde", 6))
        self.aristas.append(Arista("Verde", "Rojo", 7))
        self.aristas.append(Arista("Amarillo", "Azul", 8))
        self.aristas.append(Arista("Amarillo", "Rojo", 9))
        self.aristas.append(Arista("Amarillo", "Verde", 10))
        self.aristas.append(Arista("Amarillo", "Naranja", 11))

        self.centros.append(Centro("Blanco", 0))
        self.centros.append(Centro("Azul", 1))
        self.centros.append(Centro("Rojo", 2))
        self.centros.append(Centro("Verde", 3))
        self.centros.append(Centro("Naranja", 4))
        self.centros.append(Centro("Amarillo", 5))

        self.esquinas.append(Esquina("Blanco", "Azul", "Rojo", 0))
        self.esquinas.append(Esquina("Blanco", "Naranja", "Azul", 1))
        self.esquinas.append(Esquina("Blanco", "Verde", "Naranja", 2))
        self.esquinas.append(Esquina("Blanco", "Rojo", "Verde", 3))
        self.esquinas.append(Esquina("Amarillo", "Rojo", "Azul", 4))
        self.esquinas.append(Esquina("Amarillo", "Azul", "Naranja", 5))        
        self.esquinas.append(Esquina("Amarillo", "Naranja", "Verde", 6))
        self.esquinas.append(Esquina("Amarillo", "Verde", "Rojo", 7))
        
        self.matriz_de_piezas = [self.esquinas, self.centros, self.aristas]

    def cara(self, color):
        # Devolver piezas adyacentes a un centro
        piezas = []
        for esquina in self.esquinas:
            if color in [esquina.color1, esquina.color2, esquina.color3]:
                piezas.append(esquina)
        for centro in self.centros:
            if color in [centro.color1]:
                piezas.append(centro)
        for arista in self.aristas:
            if color in [arista.color1, arista.color2]:
                piezas.append(arista)
        return piezas
    
    def __str__(self):
        return str(self.esquinas) + "\n" + str(self.centros) + "\n" + str(self.aristas)
    
    def __repr__(self):
        return str(self.esquinas) + "\n" + str(self.centros) + "\n" + str(self.aristas)
    
    def capa_superior(self):
        return self.capa_sup
    
    def capa_media(self):
        return self.capa_mid
    
    def capa_inferior(self):
        return self.capa_inf
    
    def piezas(self):
        return self.matriz_de_piezas
    

cubo = Cubo()

print(cubo.capa_superior())

pieza = Pieza("Arista", "Blanco", "Azul", "Rojo", 0)

print(pieza)
    
# esquinas = []
# centros = []
# aristas = []

# centros.append(Centro("Blanco", 1))
# esquinas.append(Esquina("Blanco", "Azul", "Rojo", 2))
# aristas.append(Arista("Blanco", "Azul", 3))
# esquinas.append(Esquina("Blanco", "Naranja", "Azul", 4))
# aristas.append(Arista("Blanco", "Naranja", 5))
# esquinas.append(Esquina("Blanco", "Verde", "Naranja", 6))
# aristas.append(Arista("Blanco", "Verde", 7))
# esquinas.append(Esquina("Blanco", "Rojo", "Verde", 8))
# aristas.append(Arista("Blanco", "Rojo", 9))
# aristas.append(Arista("Rojo", "Azul", 10))
# centros.append(Centro("Azul", 11))
# aristas.append(Arista("Azul", "Naranja", 12))
# centros.append(Centro("Naranja", 13))
# aristas.append(Arista("Naranja", "Verde", 14))
# centros.append(Centro("Verde", 15))
# aristas.append(Arista("Rojo", "Verde", 16))
# centros.append(Centro("Rojo", 17))
# esquinas.append(Esquina("Amarillo", "Rojo", "Azul", 18))
# aristas.append(Arista("Amarillo", "Azul", 19))
# esquinas.append(Esquina("Amarillo", "Azul", "Naranja", 20))
# aristas.append(Arista("Amarillo", "Naranja", 21))
# esquinas.append(Esquina("Amarillo", "Naranja", "Verde", 22))
# aristas.append(Arista("Amarillo", "Verde", 23))
# esquinas.append(Esquina("Amarillo", "Verde", "Rojo", 24))
# aristas.append(Arista("Amarillo", "Rojo", 25))
# centros.append(Centro("Amarillo", 26))


# for i in range(1, 8):
#     print(esquinas[i])

# for i in range(1, 6):
#     print(centros[i])

# for i in range(1, 12):
#     print(aristas[i])

# cubo = Cubo(esquinas, centros, aristas)
# cara_azul = cubo.cara("Azul")
# print("---------------------")
# print("------Cara azul------")
# print("---------------------")
# for i in range(1, 9):
#     print(cara_azul[i])
# print("-------------------------")
# print("------Cara amarilla------")
# print("-------------------------")
# cara_amarilla = cubo.cara("Amarillo")
# for i in range(1, 9):
#     print(cara_amarilla[i])
# print("---------------------")
# print("------Cara roja------")
# print("---------------------")
# cara_roja = cubo.cara("Rojo")
# for i in range(1, 9):
#     print(cara_roja[i])
# print("-----------------------")
# print("------Cara blanca------")
# print("-----------------------")
# cara_blanca = cubo.cara("Blanco")
# for i in range(1, 9):
#     print(cara_blanca[i])
# print("------------------------")
# print("------Cara naranja------")
# print("------------------------")
# cara_naranja = cubo.cara("Naranja")
# for i in range(1, 9):
#     print(cara_naranja[i])
# print("------------------------")
# print("-------Cara verde-------")
# print("------------------------")
# cara_verde = cubo.cara("Verde")
# for i in range(1, 9):
#     print(cara_verde[i])