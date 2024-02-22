"""3)Write a Python class, Square, and define two methods that return the square area and perimeter."""

class square : 

    def __init__(self,length) -> None:
        self.length=length

    def sq_area(self) :
        area = self.length**2
        return area

    def sq_perimeter(self) :
        perimeter = self.length*4
        return perimeter

n=float(input("Enter the length of the square :"))

obj = square(n)

print("Area =",obj.sq_area())
print("Perimeter =",obj.sq_perimeter())