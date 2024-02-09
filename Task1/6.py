"""Python program to print all even/odd numbers in the range given by user"""

def even(a,b):
    print("Even nos :")
    for i in range(a,b+1):
        if i%2==0:
            print(i)

def odd(a,b):
    print("Odd nos :")
    for i in range(a,b+1):
        if i%2!=0:
            print(i)

 
a = int(input("Enter the start : "))
b = int(input("Enter the end : "))


even(a,b)
odd(a,b)