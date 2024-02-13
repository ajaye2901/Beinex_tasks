"""Write a Python program to create Fibonacci series up to n using Lambda. 

Fibonacci series upto 2: 

[0, 1] 

Fibonacci series upto 5: 

[0, 1, 1, 2, 3] 

Fibonacci series upto 6: 

[0, 1, 1, 2, 3, 5] """




fib=lambda n:n if n<=1 else fib(n-1)+fib(n-2)

n=int(input("Enter a No : "))
l=[]
for i in range(n):
    l.append(fib(i))

print("Fibanocci series upto",n," : ",l)
        

