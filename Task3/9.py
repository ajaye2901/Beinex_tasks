"""Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list: 

['Python', 3, 2, 4, 5, 'version'] 

Maximum values in the said list using lambda:5 """


def maximum(l) :

    k=max(filter(lambda x : type(x)==int,l))
    return k

l=['Python', 3, 2, 4, 5, 'version'] 
print("Maximum value in the list : ",maximum(l))