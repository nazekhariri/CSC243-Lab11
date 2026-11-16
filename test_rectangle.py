from Point import Point
from Rectangle import Rectangle

p1 = Point(1, 2)
p2 = Point(3.2, 4)
R = Rectangle(p1, p2)
print(R)
print(R.get_width())
print(R.get_height())
print(R.area())
print(R.perimeter())
print(R.contains(Point(1.5, 3)))
print(R.contains(Point(10.5, 3)))
print(R.contains(Point(1, 2)))
print(R.contains(Point(3.2, 4)))
