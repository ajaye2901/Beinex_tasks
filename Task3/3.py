"""Write a Python program to find if a given string starts with a given character using Lambda"""

k=lambda s,a : True if s[0]==a else False

s=input("Enter a word : ")
a=input("Enter a character : ")

print(k(s,a))