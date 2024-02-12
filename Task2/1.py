"""Write a Python function that calculates the factorial of a given integer. 
Demonstrate how to call this function with an example"""

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter a Number : "))
a=factorial(n)

print("Factorial of",n ,"is", a)