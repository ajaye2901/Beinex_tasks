"""Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results. 

Original list: [2, 4, 6, 9, 11] 

Given number: 2 

Result: 

4 8 12 18 22 """


def multiply(l,n):

    k=list(map(lambda x: x*n ,l))

    return k

l=[2,4,6,9,11]

n=int(input("Enter a No : "))

print(multiply(l,n))