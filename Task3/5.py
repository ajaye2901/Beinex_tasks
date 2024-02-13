"""Write a Python program to check whether a given string is a number or not using Lambda. """


k = lambda x : True if x.isdigit() else False

x=input("Enter a string : ")
print(k(x))

