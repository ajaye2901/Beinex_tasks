"""Write a Python program that accepts a hyphen-separated sequence of words as input and prints 
the words in a hyphen-separated sequence after sorting them alphabetically. 
Sample Items : green-red-yellow-black-white 
Expected Result : black-green-red-white-yellow """


def hy_sort(s) :
    l=s.split("-")
    l.sort()
    k='-'.join(l)
    print(k)

s=input("Enter hyphen-separated sequence of words : ")

hy_sort(s)




