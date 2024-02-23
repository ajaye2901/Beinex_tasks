# Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
# Define constructor for each of them to assign the necessary parameters required for calculating the area.
# Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
# Create an object for each of the subclasses and call the area method on the objects.

from abc import ABC,abstractmethod
import math

class Shape(ABC) :

    @abstractmethod
    def area(self) :
        raise NotImplementedError ("area method must be implemented in the subclass")

class Triangle(Shape) :

    def __init__(self,base,height) -> None:
        self.base = base
        self.height = height

    def area(self) :
        return 0.5 * self.base * self.height
    
class Square(Shape) :

    def __init__(self,side) -> None:
        self.side = side

    def area(self):
        return self.side * 2
    
class Pentagon(Shape) :

    def __init__(self,side) -> None:
        self.side = side

    def area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side ** 2
    
class Circle(Shape) :

    def __init__(self,radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
t = Triangle(2,2)
s = Square(2)
p = Pentagon(2)
c = Circle(2)

print("Area of a Triangle : ",t.area())
print("Area of a Square : ",s.area())
print("Area of a Pentagon : ",p.area())
print("Area of a Circle : ",c.area())
        

