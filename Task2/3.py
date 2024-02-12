"""Write a Python function to find the maximum of three numbers. """

def max_nos(a,b,c):
    print("maximum is",max(a,b,c))  #using max function

    if a>b and a>c:
        print("maximum is",a)

    elif b>a and b>c :
        print("maximum is",b)

    else:
        print("maximum is",c)

max_nos(4,7,6)