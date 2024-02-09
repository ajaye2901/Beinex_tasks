"""Find the sum of all even numbers between the range given by user"""

def Sum(start,end):
    sum=0
    for i in range(start,end+1):
        if i%2==0:
            sum=sum+i
    print("Sum ",sum)



start=int(input("Enter the start : "))
end=int(input("Enter the end : "))

Sum(start,end)

