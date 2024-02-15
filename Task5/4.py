"""4.Write a Python program to print the numbers of a specified listafter removing even numbers from it
	list = [24,34,53,65,78,93,23,42]"""

def remove_even_nos(l):

    odd_list=[]
    for i in l:
        if i%2!=0:
            odd_list.append(i)
    return odd_list
            

l=[24,34,53,65,78,93,23,42]
print("List after deleting even nos : ",remove_even_nos(l))




