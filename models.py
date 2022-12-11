import math

from abc import ABC, abstractmethod


class Point():
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def get_len(p1: Point, p2: Point) -> float:
    return math.sqrt(math.pow(p2.x - p1.x, 2) + math.pow(p2.y - p1.y, 2))

class Figure(ABC):
    @abstractmethod
    def get_perimeter() -> float:
        pass
    
    @abstractmethod
    def get_area() -> float:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass

class Triangle(Figure):
    len_p1_p2 : float
    len_p2_p3 : float
    len_p3_p1 : float

    def __init__(self, p1 : Point, p2 : Point, p3 : Point):
        self.len_p1_p2 = get_len(p1, p2)
        self.len_p2_p3 = get_len(p2, p3)
        self.len_p3_p1 = get_len(p3, p1)

    def get_perimeter(self) -> float:
        return self.len_p1_p2 + self.len_p2_p3 + self.len_p3_p1

    def get_area(self) -> float:
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.len_p1_p2) 
                                        * (semi_perimeter - self.len_p2_p3)
                                        * (semi_perimeter - self.len_p3_p1))

    def __str__(self) -> str:
        return 'Треугольник'

class Rectangle(Figure):
    len_p1_p2 : float
    len_p2_p3 : float
    
    def __init__(self, p1 : Point, p2 : Point, p3 : Point):
        self.len_p1_p2 = get_len(p1, p2)
        self.len_p2_p3 = get_len(p2, p3)

    def get_perimeter(self) -> float:
        return (self.len_p1_p2 + self.len_p2_p3)*2

    def get_area(self) -> float:
        return self.len_p1_p2 * self.len_p2_p3

    def __str__(self) -> str:
        return 'Прямоугольник'

class Circle(Figure):
    len_p1_p2 : float
    
    def __init__(self, p1 : Point, p2 : Point):
        self.len_p1_p2 = get_len(p1, p2)

    def get_perimeter(self) -> float:
        return 2 * self.len_p1_p2 * math.pi

    def get_area(self) -> float:
        return math.pi*math.pow(self.len_p1_p2, 2)

    def __str__(self) -> str:
        return 'Круг'