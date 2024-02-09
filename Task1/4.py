""" Python program to check the number taken as an input is even or odd,
print invalide input if user enters anything other than integers"""

def check(no):
    if no % 2 == 0:
        print(no, "is even no")
    else:
        print(no, "is odd no")

No=int(input("Enter a no"))


check(No)