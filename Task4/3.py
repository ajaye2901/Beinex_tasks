"""Write a Python code to remove all characters except a            

Sample String : 'exercises' 

Expected Result : 'eee' (Removed all characters except special character : e) """

def remove_char(s,a) :

    new_str=""
    for i in s:
        if i==a:
            new_str=new_str+i
    return new_str
     
s=input("Enter the string : ")
a=input("Enter the character : ")

print(remove_char(s,a))