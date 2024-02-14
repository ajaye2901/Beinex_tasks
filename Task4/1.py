"""Write a Python program to calculate the length of a string. """

def string_length(s):

    length=0

    for i in s:
        length=length+1
    
    return length

s=input("Enter the string : ")

print("Length of the string is",string_length(s))


#Using the built-in function

print("Length of the string is",len(s))