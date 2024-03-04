#  Write a Python function that takes a list of integers as input and returns a 
# new list with only the numbers that are perfect squares. 
import math

def PerfectSquare(Lst) :
    perfect_lst=[] 
    for item in Lst:
        if not isinstance(item,int) or item < 0 :
            continue
        sqrt_item = int(math.sqrt(item))
        if sqrt_item * sqrt_item == item :
            perfect_lst.append(item)
    return perfect_lst

Lst = [2,8,9,21,4,81,16]
print(PerfectSquare(Lst))