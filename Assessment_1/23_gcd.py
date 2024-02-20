def gcd(n1,n2):

    for i in range(1,min(n1,n2)+1):
        if n2%i == 0 and n1%i==0:
            gcd=i
    return gcd


n1=int(input("Enter first no : "))
n2=int(input("Enter second no : "))


print("GCD of",n1,"and",n2,"is",gcd(n1,n2))