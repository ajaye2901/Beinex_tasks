"""· Write a Python program to assess if a file is closed or not."""

f=open(r"C:\Users\ajuaj\Desktop\Beinex\Task7\1_read.txt","r")
f.close()

if f.closed :
    print("file is closed")
else:
    print("File is not closed")
