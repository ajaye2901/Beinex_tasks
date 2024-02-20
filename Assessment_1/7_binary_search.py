def binary(l,n):
    low=0
    high=len(l) - 1


    while low<=high:

        mid=(low+high)//2

        if n==l[mid]:
            return mid
        
        elif n < l[mid] :
            high = mid - 1
        
        else :
            low=mid + 1
    return 1




s=int(input("Enter the length of the list : "))

lst=[int(input("Enter the items :")) for i in range(s)]

l=sorted(lst)

print(l)



n=int(input("Enter the item you want to serach : "))

k=binary(l,n)

if k!=1:
    print("Element found at index",k)
else:
    print("Element not found ")

