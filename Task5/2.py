"""2.Write a Python program to remove duplicates from a list."""

def remove_duplicates(l) :

    for i in l:
        if l.count(i)>1:
            l.remove(i)
    return l

l=[1,2,3,3,1,4,5,6,5]
print("List after removing the duplicates : ",remove_duplicates(l))


