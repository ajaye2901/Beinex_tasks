"""Write a Python function that accepts a string and counts the number of upper and lower case letters"""

def counts_upper_lower(a) :
    lower=0
    upper=0

    for i in a:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
    return lower,upper
a=input("Enter a string :")

low,up=counts_upper_lower(a)
print("lowercase =",low,"uppercase = ",up)


