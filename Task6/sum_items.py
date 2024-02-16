"""4. Write a Python program to sum all the items in a dictionary"""

def sum_of_items(d):
    sum=0
    for i in d.values():
        sum=sum+i
    return sum


d={}

n=int(input("Enter the no of key and value you want : "))


for i in range(1,n+1):
    x=input("Enter the key : ")
    y=int(input("Enter the Value : "))

    d[x]=y

print(sum_of_items(d))
