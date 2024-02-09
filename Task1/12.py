"""Print first 10 fibonacci numbers using 'for' and 'while' loops"""

def fib(n):
    first=0                           
    second=1
    for i in range(0,n):
        print(first)
        third=first+second
        first=second
        second=third

fib(10)

def fib(n):
    first=0
    second=1
    while n>0:
        print(first)
        third=first+second
        first=second
        second=third
        n=n-1


fib(10)



