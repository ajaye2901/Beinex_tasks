"""3.Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3"""


def count_of_strings(l):

    count=0
    for i in l :
        if len(i)>2:
            count=count+1
    return count

l=['abc', 'xyz', 'aba', '1']
print("Count =",count_of_strings(l))