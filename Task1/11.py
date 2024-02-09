"""Find the sum of all odd numbers between the rane given by user using while loop"""


def Sum(start,end):

    sum=0
    while start<end+1:
        if start%2==0:
            sum=sum+start
        start=start+1
    print(sum)




start=int(input("Enter the start : "))
end=int(input("Enter the end : "))

Sum(start,end)