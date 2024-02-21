"""· Write a Python program to read first n lines of a file."""

n=int(input("Enter how many lines you want to read : "))

f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\1_read.txt","r")

for i in range(n) :
    print(f.readline())

f.close()