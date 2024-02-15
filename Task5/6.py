"""6.Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]"""


l=[2, 4, 6, 8, 10, 12, 14]

new_lst=[i**2 for i in l if i**2>50]

print(new_lst)