import copy
import random
from cubo import Esquina, Centro, Arista

class RubiksCube:
    def __init__(self):
        self.esquinas = [
            Esquina("W", "O", "G", 0),
            Esquina("W", "G", "R", 1),
            Esquina("W", "R", "B", 2),
            Esquina("W", "B", "O", 3),
            Esquina("Y", "G", "O", 4),
            Esquina("Y", "R", "G", 5),
            Esquina("Y", "B", "R", 6),
            Esquina("Y", "O", "B", 7)
        ]
        self.centros = [
            Centro("W", 0),
            Centro("O", 1),
            Centro("G", 2),
            Centro("R", 3),
            Centro("B", 4),
            Centro("Y", 5)
        ]
        self.aristas = [
            Arista("W", "O", 0),
            Arista("W", "G", 1),
            Arista("W", "R", 2),
            Arista("W", "B", 3),
            Arista("O", "G", 4),
            Arista("G", "R", 5),
            Arista("R", "B", 6),
            Arista("B", "O", 7),
            Arista("Y", "O", 8),
            Arista("Y", "G", 9),
            Arista("Y", "R", 10),
            Arista("Y", "B", 11)
        ]

    def __str__(self):
        return "Rubik's Cube"

    def rotate_up(self):
        esquinas_copy = copy.deepcopy(self.esquinas)
        centros_copy = copy.deepcopy(self.centros)
        aristas_copy = copy.deepcopy(self.aristas)

        self.centros[0].pos = 3
        self.centros[2].pos = 0
        self.centros[3].pos = 2
        self.centros[1].pos = 1

        self.esquinas[0].pos = 3
        self.esquinas[1].pos = 0
        self.esquinas[2].pos = 1
        self.esquinas[3].pos = 2

        self.aristas[0].pos = 3
        self.aristas[1].pos = 0
        self.aristas[2].pos = 1
        self.aristas[3].pos = 2

        self.aristas[0].color1, self.aristas[0].color2 = self.aristas[2].color2, self.aristas[2].color1
        self.aristas[1].color1, self.aristas[1].color2 = self.aristas[0].color1, self.aristas[0].color2
        self.aristas[3].color1, self.aristas[3].color2 = self.aristas[1].color2, self.aristas[1].color1
        self.aristas[2].color1, self.aristas[2].color2 = self.aristas[3].color2, self.aristas[3].color1

    def rotate_down(self):
        esquinas_copy = copy.deepcopy(self.esquinas)
        centros_copy = copy.deepcopy(self.centros)
        aristas_copy = copy.deepcopy(self.aristas)

        self.centros[0].pos = 1
        self.centros[2].pos = 2
        self.centros[3].pos = 0
        self.centros[1].pos = 3

        self.esquinas[0].pos = 1
        self.esquinas[1].pos = 2
        self.esquinas[2].pos = 3
        self.esquinas[3].pos = 0

        self.aristas[0].pos = 1
        self.aristas[1].pos = 2
        self.aristas[2].pos = 3
        self.aristas[3].pos = 0

        self.aristas[0].color1, self.aristas[0].color2 = self.aristas[1].color2, self.aristas[1].color1
        self.aristas[1].color1, self.aristas[1].color2 = self.aristas[3].color2, self.aristas[3].color1
        self.aristas[3].color1, self.aristas[3].color2 = self.aristas[2].color2, self.aristas[2].color1
        self.aristas[2].color1, self.aristas[2].color2 = self.aristas[0].color1, self.aristas[0].color2

    def rotate_left(self):
        esquinas_copy = copy.deepcopy(self.esquinas)
        centros_copy = copy.deepcopy(self.centros)
        aristas_copy = copy.deepcopy(self.aristas)

        self.centros[0].pos = 4
        self.centros[4].pos = 3
        self.centros[5].pos = 0
        self.centros[2].pos = 5

        self.esquinas[0].pos = 4
        self.esquinas[4].pos = 3
        self.esquinas[7].pos = 0
        self.esquinas[3].pos = 5

        self.aristas[1].pos = 4
        self.aristas[8].pos = 3
        self.aristas[5].pos = 0
        self.aristas[9].pos = 5

        self.aristas[1].color1, self.aristas[1].color2 = self.aristas[5].color2, self.aristas[5].color1
        self.aristas[5].color1, self.aristas[5].color2 = self.aristas[9].color2, self.aristas[9].color1
        self.aristas[9].color1, self.aristas[9].color2 = self.aristas[8].color2, self.aristas[8].color1
        self.aristas[8].color1, self.aristas[8].color2 = self.aristas[1].color1, self.aristas[1].color2

    def rotate_right(self):
        esquinas_copy = copy.deepcopy(self.esquinas)
        centros_copy = copy.deepcopy(self.centros)
        aristas_copy = copy.deepcopy(self.aristas)

        self.centros[0].pos = 5
        self.centros[4].pos = 0
        self.centros[5].pos = 3
        self.centros[2].pos = 4

        self.esquinas[0].pos = 5
        self.esquinas[4].pos = 0
        self.esquinas[7].pos = 3
        self.esquinas[3].pos = 4

        self.aristas[1].pos = 5
        self.aristas[8].pos = 0
        self.aristas[5].pos = 3
        self.aristas[9].pos = 4

        self.aristas[1].color1, self.aristas[1].color2 = self.aristas[8].color2, self.aristas[8].color1
        self.aristas[8].color1, self.aristas[8].color2 = self.aristas[9].color2, self.aristas[9].color1
        self.aristas[9].color1, self.aristas[9].color2 = self.aristas[5].color2, self.aristas[5].color1
        self.aristas[5].color1, self.aristas[5].color2 = self.aristas[1].color1, self.aristas[1].color2

    def rotate_front(self):
        esquinas_copy = copy.deepcopy(self.esquinas)
        centros_copy = copy.deepcopy(self.centros)
        aristas_copy = copy.deepcopy(self.aristas)

        self.centros[0].pos = 2
        self.centros[1].pos = 5
        self.centros[4].pos = 1
        self.centros[3].pos = 4

        self.esquinas[0].pos = 2
        self.esquinas[1].pos = 5
        self.esquinas[5].pos = 1
        self.esquinas[4].pos = 4

        self.aristas[2].pos = 2
        self.aristas[9].pos = 5
        self.aristas[6].pos = 1
        self.aristas[4].pos = 4

        self.aristas[2].color1, self.aristas[2].color2 = self.aristas[6].color2, self.aristas[6].color1
        self.aristas[6].color1, self.aristas[6].color2 = self.aristas[4].color2, self.aristas[4].color1
        self.aristas[4].color1, self.aristas[4].color2 = self.aristas[9].color2, self.aristas[9].color1
        self.aristas[9].color1, self.aristas[9].color2 = self.aristas[2].color1, self.aristas[2].color2

    def rotate_back(self):
        esquinas_copy = copy.deepcopy(self.esquinas)
        centros_copy = copy.deepcopy(self.centros)
        aristas_copy = copy.deepcopy(self.aristas)

        self.centros[0].pos = 4
        self.centros[1].pos = 2
        self.centros[4].pos = 5
        self.centros[3].pos = 3

        self.esquinas[0].pos = 4
        self.esquinas[1].pos = 2
        self.esquinas[5].pos = 5
        self.esquinas[4].pos = 3

        self.aristas[2].pos = 4
        self.aristas[9].pos = 2
        self.aristas[6].pos = 5
        self.aristas[4].pos = 3

        self.aristas[2].color1, self.aristas[2].color2 = self.aristas[9].color2, self.aristas[9].color1
        self.aristas[9].color1, self.aristas[9].color2 = self.aristas[4].color2, self.aristas[4].color1
        self.aristas[4].color1, self.aristas[4].color2 = self.aristas[6].color2, self.aristas[6].color1
        self.aristas[6].color1, self.aristas[6].color2 = self.aristas[2].color1, self.aristas[2].color2

    def shuffle(self):
        for i in range(20):
            move = random.choice(['U', 'D', 'L', 'R', 'F', 'B'])
            if move == 'U':
                self.rotate_up()
            elif move == 'D':
                self.rotate_down()
            elif move == 'L':
                self.rotate_left()
            elif move == 'R':
                self.rotate_right()
            elif move == 'F':
                self.rotate_front()
            elif move == 'B':
                self.rotate_back()

    def is_solved(self):
        for esquina in self.esquinas:
            if esquina.color1 != esquina.color2 != esquina.color3:
                return False
        for centro in self.centros:
            if centro.color1 != centro.color1:
                return False
        for arista in self.aristas:
            if arista.color1 != arista.color2:
                return False
        return True

def main():
    cube = RubiksCube()
    print(cube)  # Rubik's Cube
    # cube.shuffle()
    # print(cube.is_solved())  
    # cube.rotate_up()
    # print(cube.is_solved())  
    # cube.rotate_down()
    # print(cube.is_solved())  
    # cube.rotate_left()
    # print(cube.is_solved())  
    # cube.rotate_right()
    # print(cube.is_solved())  
    # cube.rotate_front()
    # print(cube.is_solved())  
    # cube.rotate_back()
    # print(cube.is_solved())  

if __name__ == '__main__':
    main()