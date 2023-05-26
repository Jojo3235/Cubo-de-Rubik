class Pieza(object):
    # Ajustar mas adelante pos, no es pos realmente ya que se va a mover
    def __init__(self, tipo, pos):
        self.tipo = tipo
        self.pos = pos
        
    def __str__(self):
        return self.tipo + str(self.pos)

class Esquina(Pieza):
    def __init__(self, color1, color2, color3, pos):
        super(Esquina, self).__init__("Esquina", pos)
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def __str__(self):
        return self.tipo + str(self.pos) + " " + self.color1 + " " + self.color2 + " " + self.color3
    
class Centro(Pieza):
    def __init__(self, color1, pos):
        super(Centro, self).__init__("Centro", pos)
        self.color1 = color1

    def __str__(self):
        return self.tipo + str(self.pos) + " " + self.color1
    
class Arista(Pieza):
    def __init__(self, color1, color2, pos):
        super(Arista, self).__init__("Arista", pos)
        self.color1 = color1
        self.color2 = color2

    def __str__(self):
        return self.tipo + str(self.pos) + " " + self.color1 + " " + self.color2
    
class Cubo(object):
    def __init__(self, esquinas: list, centros: list, aristas: list):
        self.esquinas = esquinas
        self.centros = centros
        self.aristas = aristas

    def cara(self, color):
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
    
esquinas = []
centros = []
aristas = []

centros.append(Centro("Blanco", 1))
esquinas.append(Esquina("Blanco", "Azul", "Rojo", 2))
aristas.append(Arista("Blanco", "Azul", 3))
esquinas.append(Esquina("Blanco", "Naranja", "Azul", 4))
aristas.append(Arista("Blanco", "Naranja", 5))
esquinas.append(Esquina("Blanco", "Verde", "Naranja", 6))
aristas.append(Arista("Blanco", "Verde", 7))
esquinas.append(Esquina("Blanco", "Rojo", "Verde", 8))
aristas.append(Arista("Blanco", "Rojo", 9))
aristas.append(Arista("Rojo", "Azul", 10))
centros.append(Centro("Azul", 11))
aristas.append(Arista("Azul", "Naranja", 12))
centros.append(Centro("Naranja", 13))
aristas.append(Arista("Naranja", "Verde", 14))
centros.append(Centro("Verde", 15))
aristas.append(Arista("Rojo", "Verde", 16))
centros.append(Centro("Rojo", 17))
esquinas.append(Esquina("Amarillo", "Rojo", "Azul", 18))
aristas.append(Arista("Amarillo", "Azul", 19))
esquinas.append(Esquina("Amarillo", "Azul", "Naranja", 20))
aristas.append(Arista("Amarillo", "Naranja", 21))
esquinas.append(Esquina("Amarillo", "Naranja", "Verde", 22))
aristas.append(Arista("Amarillo", "Verde", 23))
esquinas.append(Esquina("Amarillo", "Verde", "Rojo", 24))
aristas.append(Arista("Amarillo", "Rojo", 25))
centros.append(Centro("Amarillo", 26))


for i in range(1, 8):
    print(esquinas[i])

for i in range(1, 6):
    print(centros[i])

for i in range(1, 12):
    print(aristas[i])

cubo = Cubo(esquinas, centros, aristas)
cara_azul = cubo.cara("Azul")
print("---------------------")
print("------Cara azul------")
print("---------------------")
for i in range(1, 9):
    print(cara_azul[i])
print("-------------------------")
print("------Cara amarilla------")
print("-------------------------")
cara_amarilla = cubo.cara("Amarillo")
for i in range(1, 9):
    print(cara_amarilla[i])
print("---------------------")
print("------Cara roja------")
print("---------------------")
cara_roja = cubo.cara("Rojo")
for i in range(1, 9):
    print(cara_roja[i])
print("-----------------------")
print("------Cara blanca------")
print("-----------------------")
cara_blanca = cubo.cara("Blanco")
for i in range(1, 9):
    print(cara_blanca[i])
print("------------------------")
print("------Cara naranja------")
print("------------------------")
cara_naranja = cubo.cara("Naranja")
for i in range(1, 9):
    print(cara_naranja[i])
print("------------------------")
print("-------Cara verde-------")
print("------------------------")
cara_verde = cubo.cara("Verde")
for i in range(1, 9):
    print(cara_verde[i])