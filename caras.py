class Edge:
    def __init__(self, color1, color2):
        self.colors = [color1, color2]

class Corner:
    def __init__(self, color1, color2, color3):
        self.colors = [color1, color2, color3]

class Center:
    def __init__(self, color):
        self.color = color

class RubiksCube:
    def __init__(self):
        self.edges = [
            [Edge('white', 'red'), Edge('white', 'blue'), Edge('white', 'orange'), Edge('white', 'green')],
            [Edge('yellow', 'red'), Edge('yellow', 'blue'), Edge('yellow', 'orange'), Edge('yellow', 'green')],
            [Edge('blue', 'red'), Edge('blue', 'orange'), Edge('green', 'red'), Edge('green', 'orange')]
        ]
        self.corners = [
            [Corner('white', 'red', 'blue'), Corner('white', 'blue', 'orange'), Corner('white', 'orange', 'green'), Corner('white', 'green', 'red')],
            [Corner('yellow', 'red', 'blue'), Corner('yellow', 'blue', 'orange'), Corner('yellow', 'orange', 'green'), Corner('yellow', 'green', 'red')]
        ]
        self.centers = [
            [Center('white'), Center('red'), Center('blue')],
            [Center('yellow'), Center('orange'), Center('green')]
        ]