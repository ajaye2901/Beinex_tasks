# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

lst = [1,2,4]
try :
    print(lst[3])
except IndexError as e :
    print("Index is out of range",e)