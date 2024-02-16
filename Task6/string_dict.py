"""8 .Create a function that takes a string and returns a dictionary where keys are letters, 
and values are the number of times each letter appears in the string  """


s=input("Enter the string")

d={}

for i in s:
    k=s.count(i)
    d[i]=k
print(d)

