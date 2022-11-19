from models import *

p1 = Point(1, 2)
p2 = Point(3, 4)

len = Figure.get_len(p1, p2)
print(len)

p3 = Point(6, 8)
fig = Triangle(p1, p2, p3)

per = fig.get_perimeter()
area = fig.get_area()

print(per)
print(area)