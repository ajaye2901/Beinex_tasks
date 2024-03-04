# 6. Write a Python function that takes a list of strings as input and returns a 
# new list with the strings sorted in descending order of their lengths.

lst = ["hello",'hi','a',"eehdid"]
lst1=sorted(lst,key=len,reverse=True)
print(lst1)