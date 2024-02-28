# 1.Write a Python program that prompts the user to enter an 
# integer and handles the ValueError exception if the user enters a non-integer value.

try :
    num = int(input("Enter a Number : "))

except ValueError :
    print("Error !!!! Enter an Integer")