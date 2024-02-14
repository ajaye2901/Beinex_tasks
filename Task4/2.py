"""Print even length words in a string. 

Sample String : ''I love coding" 

Expected Result : “love, coding” """


def even_length(s):
    
    k=s.split()
    z=[]
    for i in k:
        if len(i) % 2 == 0 :
            z.append(i)
    a=", ".join(z)
    return a
            
s=input("Enter the string : ")
print(even_length(s))

