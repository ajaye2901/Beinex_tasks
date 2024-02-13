"""Write a Python program to extract year, month, date and time using Lambda. 
Sample Output: 

2020-01-15 09:03:32.744178 

2020 

1 

15 

09:03:32.744178 
"""


import datetime

def extract(x):
    a=lambda k : k.year

    b=lambda k : k.month

    c=lambda k : k.day

    d=lambda k : k.time()

    return a(x),b(x),c(x),d(x)

x=datetime.datetime.now()

year,month,day,time=extract(x)
print(year)
print(month)
print(day)
print(time)


