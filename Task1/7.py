"""Python program to print the multiplication table of any number
(number should be taken as input and user decides the end limit of the table)"""


def multiplication(n,limit) :

    for i in range(1,limit+1):
        print(i, "*", n, "=", i*n)

n=int(input("Enter the number : "))
limit=int(input("Enter the limit of the table"))

multiplication(n,limit)