"""3. Write a Python program to print a dictionary 
where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys """


d={}

for i in range(1,16):
    d[i]=i**2

print(d)