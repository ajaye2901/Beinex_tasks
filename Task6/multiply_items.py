"""5. Write a Python program to multiply all the items in a dictionary. """

l1=["a","b","c","d"]
l2=[2,4,6,8]

d1=dict(zip(l1,l2))

mul=1
for i in d1.values() :
    mul=mul*i
print("Product of all items in the dictionary is",mul)