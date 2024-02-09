""" Write python programs , which accept two inputs and perform the following arithmetic operations
	i)    Addition (+)
        ii)   Subtraction (-)
        iii)  Multiplication (*)
        iv)   Division (/)
        v)    Modulus (%)
        vi)   Exponentiation (**)
        vii)  Floor Division (//)  """

a=float(input("Enter first no : "))
b=float(input("Enter the second no : "))

print("Sum is ", a+b)
print("Difference is ",a-b)
print("Product is ",a*b)
print("Division is ",a/b)                  # I am aware of the divided by zero case. 
print("Reminder is  ",a%b)                 # I am aware of the divided by zero case.
print("Exponential is ",a**b)
print("Floor Division is ",a//b)           # I am aware of the divided by zero case.

