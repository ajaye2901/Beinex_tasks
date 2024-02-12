"""Define a function that accepts 2 values and return its sum, subtraction and multiplication.
 Using 4 types of functions based on arguments and return type. """


# 1. Without argument and return

def func1():
    x=int(input("Enter the first no : "))
    y=int(input("Enter the second no : "))

    print("Sum = ",x+y)
    print("Subtraction = ",x-y)
    print("Multiplication = ",x*y)

func1()

#with argument and no return

def func2(a,b):
    print("Sum = ",a+b)
    print("Subtraction = ",a-b)
    print("Multiplication = ",a*b)

a=int(input("Enter the first no : "))
b=int(input("Enter the second no : "))

func2(a,b)

#no argument with return

def func3():
    x=int(input("Enter the first no : "))
    y=int(input("Enter the second no : "))

    Sum = x+y
    Subtraction = x-y
    Multiplication = x*y

    return Sum,Subtraction,Multiplication

Sum,Subtraction,Multiplication=func3()
print("Sum = ",Sum,"\n","Subtraction = ",Subtraction,"\n","Multiplication = ",Multiplication)

#with argument and return

def func4(a,b) :

    Sum = a+b
    Subtraction = a-b
    Multiplication = a*b

    return Sum,Subtraction,Multiplication

a=int(input("Enter the first no : "))
b=int(input("Enter the second no : "))

Sum,Subtraction,Multiplication=func4(a,b)
print("Sum = ",Sum,"\n","Subtraction = ",Subtraction,"\n","Multiplication = ",Multiplication)



