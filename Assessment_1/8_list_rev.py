s=int(input("Enter the length of the list : "))

lst=[int(input("Enter the items :")) for i in range(s)]

rev = lst[::-1]

print("List before reversing",lst)
print("List after reversing",rev)