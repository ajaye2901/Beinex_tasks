"""Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. 
Then, in another Python script, import the module and use the function to calculate the area 
of a rectangle with specific dimensions."""

import area_rect 

x=float(input("Enter the length : "))
y=float(input("Enter the Width : "))

a=area_rect.area_rectangle(x,y)

print("Area = ",a)