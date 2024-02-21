"""Write a Python program to copy the contents of a file to another file."""


f1=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\1_read.txt","r")

contents=f1.read()
f1.close()

f2=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\2_copy.txt","w+")

f2.write(contents)
f2.close()
