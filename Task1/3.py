""" Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same"""

def greatest(a,b,c) :

    if a==b==c:
        print("All 3 nos are same")
    else:
        if a>b and a>c:
            print(a, "is the largest no")
        elif b>a and b>c:
            print(b ,"is the largest no")
        else:
            print(c ,"is the largest no")


a=float(input("Enter first no :"))
b=float(input("Enter second no :"))
c=float(input("Enter third no :"))

greatest(a,b,c)
