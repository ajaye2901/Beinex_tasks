""" Write a Python program to read a file line by line store it into a variable."""

f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\1_read.txt","r")

s=''

for i in f:
    s=s+i
f.close()

print(s)

