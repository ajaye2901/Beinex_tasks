"""
	        *
           * *
          * * *
         * * * *
"""

def pattern_a(n):

    for i in range(n):
        for k in range(n-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()

pattern_a(4)

"""
        o
		1 2
		3 4 5
		6 7 8 9
"""

def pattern_b(n):
    num=0
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=" ")
            num=num+1
        print()

pattern_b(4)


"""
	    o
		1 1
		2 2 2
		3 3 3 3
"""

def pattern_b(n):
    num=0
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=" ")
        num=num+1
        print()

pattern_b(4)

"""
	    *
		* *
		* * *
		* * * *
"""

def pattern_b(n):
    num=0
    for i in range(1,n+1):
        print("*"*i)

pattern_b(4)