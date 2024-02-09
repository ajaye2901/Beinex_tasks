"""Find the factorial of a number taken as input using while loop"""

def factorial(n):
    
    fact=1
    i=1
    while n>0:
        fact=fact*i
        i=i+1
        n=n-1
    print(fact)


n=int(input("Enter a no : "))

factorial(n)