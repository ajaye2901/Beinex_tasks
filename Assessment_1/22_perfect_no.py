def perfect_no(n):
    if n>0:
        sum=0
        for i in range(1,n):
            if n%i==0:
                sum+=i
        return sum
    else:
        return 0




n = int(input("Enter your no : "))

k=perfect_no(n)

if k != 0:
    
    if k==n:
        print(n,"is a perfect no ")

    else:
        print("not a perfect no")
