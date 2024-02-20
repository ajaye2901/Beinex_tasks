s=int(input("Enter the length of the list : "))

lst=[int(input("Enter the items :")) for i in range(s)]

lst.sort()

print("second largest element is ",lst[-2])