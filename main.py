from models import *
from prettytable import PrettyTable
from typing import List

def print_table(figures: List[Figure]) -> None:
    table = PrettyTable(['Номер', 'Название', 'Периметр', 'Площадь'])

    for i in range(len(figures)):
        table.add_row([i + 1, figures[i], round(figures[i].get_perimeter(), 2), round(figures[i].get_area(), 2)])
    
    print(table)

if __name__ == '__main__':
    figures = list()
    points = list() 

    amount_figures = int(input("Введите количество нужных фигур: "))

    while amount_figures:
        type_figure = input("Введите тип фигуры (triangle/rectangle/circle): ")

        if type_figure == 'triangle':
            print("Треугольник")
            
            x1, y1, x2, y2, x3, y3 = map(int, input(f"Введите координаты трех точек (через пробел: x1 y1 ...): ").split())

            type_figure = Triangle(Point(x1,y1), Point(x2,y2), Point(x3,y3))
        
        if type_figure == 'rectangle':
            print("Четырехугольник")

            x1, y1, x2, y2, x3, y3 = map(int, input(f"Введите координаты трех точек (через пробел: x1 y1 ...): ").split())

            type_figure = Rectangle(Point(x1,y1), Point(x2,y2), Point(x3,y3))
            
        if type_figure == 'circle':
            print("Круг")

            x1, y1, x2, y2 = map(int, input(f"Введите координаты двух точек (через пробел: x1 y1 ...): ").split())

            type_figure = Circle(Point(x1,y1), Point(x2,y2))
            
        figures.append(type_figure)

        amount_figures -= 1

        if not amount_figures: 
            break

    print_table(figures=figures)