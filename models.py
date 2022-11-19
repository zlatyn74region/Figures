import math

from abc import ABC, abstractmethod


class Point():
    x : float
    y : float

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure(ABC):
    @abstractmethod
    def get_perimeter():
        pass
    
    @abstractmethod
    def get_area():
        pass
    
    @staticmethod
    def get_len(p1 : Point, p2 : Point):
        return math.sqrt(math.pow(p2.x - p1.x, 2) + math.pow(p2.y - p1.y, 2))

    @abstractmethod
    def __str__(self) -> str:
        pass

class Triangle(Figure):
    len_p1_p2 : float
    len_p2_p3 : float
    len_p3_p1 : float

    def __init__(self, p1 : Point, p2 : Point, p3 : Point):
        self.len_p1_p2 = super().get_len(p1, p2)
        self.len_p2_p3 = super().get_len(p2, p3)
        self.len_p3_p1 = super().get_len(p3, p1)

    def get_perimeter(self):
        return self.len_p1_p2 + self.len_p2_p3 + self.len_p3_p1

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.len_p1_p2) 
                                        * (semi_perimeter - self.len_p2_p3)
                                        * (semi_perimeter - self.len_p3_p1))

    def __str__(self) -> str:
        return 'Треугольник'