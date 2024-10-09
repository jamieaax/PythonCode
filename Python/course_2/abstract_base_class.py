
from abc import ABC, abstractmethod

class GraphicShape(ABC): #ABC prevents GraphicShape from being instaniated
    def __init__(self):
        super().__init__()

    #GraphicShape's child classes must inherit its calcArea abstract method
    @abstractmethod 
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())