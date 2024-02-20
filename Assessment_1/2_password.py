import re

def password_valid(s):

    if len(s)<8:
        return False,"length is less than 8"

    if not re.search('[a-z]',s):
        return False,"missing lower case"

    if not re.search('[A-Z]',s):
        return False,"missing upper case"
    
    if not re.search('[@$_]',s):
        return False,"missing special character"
    
    if not re.search('[0-9]',s):
        return False,"missing nos"

    return True,"Valid"

s=input("Enter the Password :")

i,j=password_valid(s)

if i==True:
    print("Valid Password")

else:
    print("Not valid",j)

    
        