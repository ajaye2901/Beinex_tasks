"""Write a Python function that takes a number as a parameter and checks whether the number is prime or not. """

def check_prime(n) :
    if n==1:
        print(n,"is not prime")
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime")
            break
    else:
        print(n,"is prime")

n=int(input("Enter a no : "))
check_prime(n)
