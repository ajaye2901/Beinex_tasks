s=int(input("Enter the length of the list : "))

lst=[int(input("Enter the items :")) for i in range(s)]

sum=0
for i in lst :
    if i%2==0:
        sum=sum+i
print(sum)