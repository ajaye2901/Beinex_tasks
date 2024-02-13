"""Write a Python program to find palindromes in a given list of strings using Lambda. """


def palindrome(l):

    k=list(filter(lambda x:  x==x[::-1],l))

    return k

l=["malayalam","ajay","civic"]
print(palindrome(l))