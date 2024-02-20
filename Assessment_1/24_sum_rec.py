def sum_items(lst):

    if len(lst) == 0:
        return 0
    
    else:
        return lst[0]+sum_items(lst[1:])



s=int(input("Enter the length of the list : "))

lst=[int(input("Enter the items :")) for i in range(s)]

print("sum is ",sum_items(lst))

