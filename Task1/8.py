"""Find the factorial of a number taken as input using for loop"""

def factorial(n) :
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of ",n, "is", fact)

n=int(input("Enter a no : "))

factorial(n)