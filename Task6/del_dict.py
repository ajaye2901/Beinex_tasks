"""7. Write a Python program to Delete a list of keys from a dictionary """


def key_name(d):
    l=[]
    n=int(input("Enter the no of keys you want to delete : "))
    if n<=len(d):
        for i in range (1,len(d)):
            x=input("Enter the Key name : ")
            l.append(x)
        return l
    else:
        return None
        

def keys_delete(d1):

    l=key_name(d1)

    if l is None:
        return 1

    else:
        for i in l:
            if i in d1.keys():
                d1.pop(i)
            else:
                return 1
        return d1
            


d1={'key1':['a','b','c','d','e'],'key2':[4,5,2,8,3],'key3':[True,False,False,True,True]}
print(d1)

k=keys_delete(d1)

if k==1:
    print("Enter correct details")

else:
    print("Dictionary after deleting the keys : ",d1)




