"""1.Write a Python program to multiples all the items in a list."""

def list_multi(l) :

    mul=1
    for i in l :
        mul=mul*i
    return mul

l=[1,3,5,7]
print("Multiples of all the items in the list",list_multi(l))
