class Pieza(object):
    def __init__(self, tipo, color1=None, color2=None, color3=None, color4=None, color5=None, color6=None):
        self.tipo = tipo
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        self.color5 = color5
        self.color6 = color6
        self.colores = [color1, color2, color3, color4, color5, color6]

    def __str__(self):
        respuesta = f"{self.tipo} "
        for color in self.colores:
            if color is not None:
                respuesta += f"{color} "
        return respuesta


class Cubo(object):
    def __init__(self):
        self.piezas_superiores = [
            [Pieza("Esquina", "Blanco", "Rojo", "Azul"), Pieza("Centro", "Blanco"), Pieza("Esquina", "Blanco", "Verde", "Rojo")],
            [Pieza("Centro", "Rojo"), None, Pieza("Centro", "Verde")],
            [Pieza("Esquina", "Rojo", "Amarillo", "Verde"), Pieza("Centro", "Amarillo"), Pieza("Esquina", "Azul", "Amarillo", "Verde")]
        ]
        self.piezas_medias = [
            [Pieza("Centro", "Azul"), None, Pieza("Centro", "Verde")],
            [None, None, None],
            [Pieza("Centro", "Azul"), None, Pieza("Centro", "Verde")]
        ]
        self.piezas_inferiores = [
            [Pieza("Esquina", "Naranja", "Verde", "Blanco"), Pieza("Centro", "Naranja"), Pieza("Esquina", "Naranja", "Azul", "Verde")],
            [Pieza("Centro", "Blanco"), None, Pieza("Centro", "Amarillo")],
            [Pieza("Esquina", "Rojo", "Amarillo", "Naranja"), Pieza("Centro", "Amarillo"), Pieza("Esquina", "Azul", "Amarillo", "Naranja")]
        ]

    def __str__(self):
        respuesta = ""
        for fila in self.piezas_superiores:
            for pieza in fila:
                if pieza is not None:
                    respuesta += "[" + str(pieza) + "]" + " "
                else:
                    respuesta += "None"
            respuesta += "\n"
        for fila in self.piezas_medias:
            for pieza in fila:
                if pieza is not None:
                    respuesta += "[" + str(pieza)  + "]" + " "
                else:
                    respuesta += "None"
            respuesta += "\n"
        for fila in self.piezas_inferiores:
            for pieza in fila:
                if pieza is not None:
                    respuesta += "[" + str(pieza)  + "]" + " "
                else:
                    respuesta += "None"
            respuesta += "\n"
        return respuesta

    def R(self):
        # Guardar piezas afectadas
        esquina1 = self.piezas_superiores[0][2]
        esquina2 = self.piezas_superiores[2][2]
        esquina3 = self.piezas_inferiores[0][2]
        esquina4 = self.piezas_inferiores[2][2]
        centro1 = self.piezas_superiores[1][2]
        centro2 = self.piezas_medias[1][2]
        centro3 = self.piezas_inferiores[1][2]

        # Mover piezas
        self.piezas_superiores[0][2] = esquina3
        self.piezas_superiores[2][2] = esquina1
        self.piezas_inferiores[0][2] = esquina4
        self.piezas_inferiores[2][2] = esquina2
        self.piezas_superiores[1][2] = centro1
        self.piezas_medias[1][2] = centro2
        self.piezas_inferiores[1][2] = centro3

    def L(self):
        # Guardar piezas afectadas
        esquina1 = self.piezas_superiores[0][0]
        esquina2 = self.piezas_superiores[2][0]
        esquina3 = self.piezas_inferiores[0][0]
        esquina4 = self.piezas_inferiores[2][0]
        centro1 = self.piezas_superiores[1][0]
        centro2 = self.piezas_medias[1][0]
        centro3 = self.piezas_inferiores[1][0]

        # Mover piezas
        self.piezas_superiores[0][0] = esquina2
        self.piezas_superiores[2][0] = esquina4
        self.piezas_inferiores[0][0] = esquina1
        self.piezas_inferiores[2][0] = esquina3
        self.piezas_superiores[1][0] = centro3
        self.piezas_medias[1][0] = centro2
        self.piezas_inferiores[1][0] = centro1

    def U(self):
        # Guardar piezas afectadas
        esquina1 = self.piezas_superiores[0][0]
        esquina2 = self.piezas_superiores[0][2]
        esquina3 = self.piezas_superiores[2][0]
        esquina4 = self.piezas_superiores[2][2]
        centro1 = self.piezas_superiores[0][1]
        centro2 = self.piezas_medias[0][1]
        centro3 = self.piezas_superiores[2][1]

        # Mover piezas
        self.piezas_superiores[0][0] = esquina2
        self.piezas_superiores[0][2] = esquina1
        self.piezas_superiores[2][0] = esquina4
        self.piezas_superiores[2][2] = esquina3
        self.piezas_superiores[0][1] = centro1
        self.piezas_medias[0][1] = centro2
        self.piezas_superiores[2][1] = centro3

    def D(self):
        # Guardar piezas afectadas
        esquina1 = self.piezas_inferiores[0][0]
        esquina2 = self.piezas_inferiores[0][2]
        esquina3 = self.piezas_inferiores[2][0]
        esquina4 = self.piezas_inferiores[2][2]
        centro1 = self.piezas_inferiores[0][1]
        centro2 = self.piezas_medias[2][1]
        centro3 = self.piezas_inferiores[2][1]

        # Mover piezas
        self.piezas_inferiores[0][0] = esquina2
        self.piezas_inferiores[0][2] = esquina1
        self.piezas_inferiores[2][0] = esquina4
        self.piezas_inferiores[2][2] = esquina3
        self.piezas_inferiores[0][1] = centro1
        self.piezas_medias[2][1] = centro2
        self.piezas_inferiores[2][1] = centro3

    def F(self):
        # Guardar piezas afectadas
        esquina1 = self.piezas_superiores[2][0]
        esquina2 = self.piezas_superiores[2][2]
        esquina3 = self.piezas_inferiores[0][0]
        esquina4 = self.piezas_inferiores[0][2]
        centro1 = self.piezas_superiores[1][0]
        centro2 = self.piezas_medias[1][0]
        centro3 = self.piezas_inferiores[1][2]

        # Mover piezas
        self.piezas_superiores[2][0] = esquina4
        self.piezas_superiores[2][2] = esquina3
        self.piezas_inferiores[0][0] = esquina2
        self.piezas_inferiores[0][2] = esquina1
        self.piezas_superiores[1][0] = centro3
        self.piezas_medias[1][0] = centro2
        self.piezas_inferiores[1][2] = centro1

    def B(self):
        # Guardar piezas afectadas
        esquina1 = self.piezas_superiores[0][0]
        esquina2 = self.piezas_superiores[0][2]
        esquina3 = self.piezas_inferiores[2][0]
        esquina4 = self.piezas_inferiores[2][2]
        centro1 = self.piezas_superiores[1][2]
        centro2 = self.piezas_medias[1][2]
        centro3 = self.piezas_inferiores[1][0]

        # Mover piezas
        self.piezas_superiores[0][0] = esquina2
        self.piezas_superiores[0][2] = esquina1
        self.piezas_inferiores[2][0] = esquina4
        self.piezas_inferiores[2][2] = esquina3
        self.piezas_superiores[1][2] = centro3
        self.piezas_medias[1][2] = centro2
        self.piezas_inferiores[1][0] = centro1

    def M(self):
        # Guardar piezas afectadas
        centro1 = self.piezas_superiores[0][1]
        centro2 = self.piezas_medias[0][1]
        centro3 = self.piezas_inferiores[0][1]
        centro4 = self.piezas_superiores[2][1]
        centro5 = self.piezas_medias[2][1]
        centro6 = self.piezas_inferiores[2][1]

        # Mover piezas
        self.piezas_superiores[0][1] = centro3
        self.piezas_medias[0][1] = centro2
        self.piezas_inferiores[0][1] = centro1
        self.piezas_superiores[2][1] = centro6
        self.piezas_medias[2][1] = centro5
        self.piezas_inferiores[2][1] = centro4

    def E(self):
        # Guardar piezas afectadas
        centro1 = self.piezas_superiores[1][0]
        centro2 = self.piezas_medias[1][0]
        centro3 = self.piezas_inferiores[1][0]
        centro4 = self.piezas_superiores[1][2]
        centro5 = self.piezas_medias[1][2]
        centro6 = self.piezas_inferiores[1][2]

        # Mover piezas
        self.piezas_superiores[1][0] = centro3
        self.piezas_medias[1][0] = centro2
        self.piezas_inferiores[1][0] = centro1
        self.piezas_superiores[1][2] = centro6
        self.piezas_medias[1][2] = centro5
        self.piezas_inferiores[1][2] = centro4

    def S(self):
        # Guardar piezas afectadas
        centro1 = self.piezas_superiores[0][0]
        centro2 = self.piezas_medias[0][0]
        centro3 = self.piezas_inferiores[0][0]
        centro4 = self.piezas_superiores[2][2]
        centro5 = self.piezas_medias[2][2]
        centro6 = self.piezas_inferiores[2][2]

        # Mover piezas
        self.piezas_superiores[0][0] = centro3
        self.piezas_medias[0][0] = centro2
        self.piezas_inferiores[0][0] = centro1
        self.piezas_superiores[2][2] = centro6
        self.piezas_medias[2][2] = centro5
        self.piezas_inferiores[2][2] = centro4

cubo = Cubo()

print(cubo)

cubo.R()

print(cubo)