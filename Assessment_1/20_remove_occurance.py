def remove_duplicates(l,k) :

    for i in l:
        if k in l and l.count(k)>1:
            l.remove(k)
    return l

l=[1,2,3,3,1,4,5,6,5]

k=int(input('Enter the element you want to remove : '))
print("List after removing the duplicates : ",remove_duplicates(l,k))