"""Write a Python program to write a list to a file."""

l=[1,2,4,5]

f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\2_copy.txt","w+")

for i in l:
    f.write(str(i)+"\n")
f.close()