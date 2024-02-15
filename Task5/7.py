"""7. Write a Python program to find the repeated items of a tuple."""

def repeated_items(t):

    l=[]
    for i in t :
        if t.count(i)>1 and i not in l:
            l.append(i)
    return l
            

t=(1,22,22,4,23,4,6)
print(repeated_items(t))